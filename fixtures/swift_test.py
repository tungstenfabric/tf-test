from future import standard_library
from builtins import object
import os
import openstack
import hashlib
from urllib.parse import urlparse
from common.openstack_libs import swift_client
from tcutils.util import custom_dict, get_random_name
from fabric.context_managers import settings, hide, cd, shell_env
from fabric.api import run, local, env
from fabric.operations import get, put
from tcutils.cfgparser import parse_cfg_file
import yaml

MODELS = {'mx240-series': ['mx240', 'mx480', 'mx960'],
          'mx10003': ['mx10003'],
          'mx204': ['mx204'],
          'qfx51xx': ['qfx5110-48s-4c', 'qfx5120-48y-8c',
                      'qfx5120-48t-6c', 'qfx5120-32c'],
          'qfx10k-series': ['qfx10002-36q', 'qfx10002-72q'],
          'qfx10k-60c': ['qfx10002-60c'],
          'qfx5100': ['qfx5100-48s-6q']}

class SwiftHelper(object):
    def __init__(self, auth_h=None, **kwargs):
        self.inputs = kwargs.get('inputs')
        self.obj = None
        self.logger = kwargs.get('logger') or self.inputs.logger if self.inputs \
            else contrail_logging.getLogger(__name__)
        if not auth_h:
            auth_h = self.get_auth_h(**kwargs)
        self.auth_h = auth_h
        self.images_info = parse_cfg_file('configs/device_images.cfg')
        self.images_dir = os.path.realpath(os.path.join(
            os.path.dirname(os.path.realpath(__file__)), '..', 'images'))
        self.container_name = None
        self.installed_images = {}
        self.models = dict()
        for key, items in MODELS.items():
            for item in items:
                self.models[item] = key
        self.device_images_cfg = custom_dict(self.get_device_images_config,
                        'device_images')
    # end __init__

    def get_device_images_config(self, key):
        if key not in self.device_images_cfg:
            image_info = self.images_info[key]
            webserver = image_info['webserver'] or self.inputs.image_web_server
            location = image_info['location']
            base_url = 'http://%s/%s' % (webserver, location)
            url = base_url+'/'+image_info['config_file']
            device_images_cfg_file = self.download_image(url)
            with open(device_images_cfg_file, 'r') as fd:
                self.device_images_cfg.update(yaml.load(fd))
        return self.device_images_cfg[key]

    def get_auth_h(self, **kwargs):
        return openstack.OpenstackAuth(**kwargs)

    def setUp(self):
        try:
            self.obj = swift_client.Connection(
                session=self.auth_h.get_session(scope='project'))
        except:
            self.logger.error("Failed to establish connection to swift")

    def create_container(self):
        if not self.container_name:
            self.container_name = get_random_name('contrail-container')
            headers = {'X-Container-Read': ".r:*,.rlistings"}
            self.obj.put_container(self.container_name, headers)
            self.logger.info("Created swift container - {}".format(
                self.container_name))

    def get_image_name(self, image_path):
        filename = os.path.basename(image_path)
        return filename.strip('.tgz')

    def delete_image(self, image_info):
        try:
            self.obj.delete_object(self.container_name, image_info['name'])
        except:
            pass

    def create_object(self, image_path, model):
        self.create_container()
        content_type = None
        object_extension = self.get_filetype(image_path)
        if object_extension == '.tgz':
            content_type = 'application/x-tar'
        sha1 = self.get_sha1(image_path)
        md5 = self.get_md5(image_path)

        image_info = self.images_info[self.models[model]]
        image_name = self.get_image_name(image_path)
        with open(image_path, 'rb') as content:
            resp = self.obj.put_object(self.container_name, image_name,
                                       content, content_type=content_type,
                                       headers={
                                           'X-Object-Meta-md5': md5,
                                           'X-Object-Meta-sha1': sha1})
        self.logger.info("Created swift object - {}".format(image_name))
        file_url = "/%s/%s"%(self.container_name, image_name)
        download_url = self.obj.url + file_url
        device_image_url = urlparse(download_url).path
        if type(image_info['supported_platforms']) is list:
            supported_platforms = image_info['supported_platforms']
        else:
            supported_platforms = [image_info['supported_platforms']]
        object_info = {'name': image_name,
            'md5': md5,
            'sha1': sha1,
            'filename': os.path.basename(image_path),
            'public_url': device_image_url,
            'supported_platforms': supported_platforms,
            'device_family': image_info['device_family']}
        self.installed_images[image_name] = object_info

    def get_filetype(self, abs_file_path):
        _, file_extension = os.path.splitext(abs_file_path)
        return file_extension

    def get_md5(self, filepath):
        hasher = hashlib.md5()
        with open(filepath, 'rb') as file_to_upload:
            temp_buffer = file_to_upload.read(65536)
            while len(temp_buffer) > 0:
                hasher.update(temp_buffer)
                temp_buffer = file_to_upload.read(65536)
        return hasher.hexdigest()
    # end get_md5

    def get_sha1(self, filepath):
        hasher = hashlib.sha1()
        with open(filepath, 'rb') as file_to_upload:
            temp_buffer = file_to_upload.read(65536)
            while len(temp_buffer) > 0:
                hasher.update(temp_buffer)
                temp_buffer = file_to_upload.read(65536)
        return hasher.hexdigest()
    # end get_sha1

    def get_base_url(self, key):
        image_info = self.images_info[key]
        webserver = image_info['webserver'] or self.inputs.image_web_server
        location = image_info['location']
        return 'http://%s/%s' % (webserver, location)

    def get_available_versions(self, model):
        key = self.models[model]
        return list(self.device_images_cfg[key].keys())

    def get_image_url(self, model, version):
        key = self.models[model]
        base_url = self.get_base_url(key)
        image = self.device_images_cfg[key][version]
        return base_url+'/'+image

    def get_image_details(self, model, version):
        image_url = self.get_image_url(model, version)
        image_name = self.get_image_name(image_url)
        if image_name not in self.installed_images.keys():
            self._install_image(image_url, model)
        return self.installed_images[image_name]

    def _install_image(self, image_url, model):
        self.logger.debug('Installing image %s' % image_url)
        img_abs_path = self.download_image(image_url)
        self.create_object(img_abs_path, model)

    def download_image(self, image_url, folder='/tmp'):
        basename = os.path.basename(image_url)
        filename = '%s/%s'%(folder, basename)
        local('mkdir -p %s'%folder)
        if not os.path.exists(filename):
            self.execute_cmd_with_proxy(
                "wget %s -O %s" % (image_url, filename))
        return filename

    def execute_cmd_with_proxy(self, cmd):
        if self.inputs.http_proxy:
            with shell_env(http_proxy=self.inputs.http_proxy):
                local(cmd)
        else:
            local(cmd)
