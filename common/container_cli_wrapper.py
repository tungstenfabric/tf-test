import random

class DockerWrapper:

    def __init__(self, inputs):
        self.inputs = inputs
        self.tool = 'docker'

    def get_active_containers(self, host):
        cmd = self.tool + \
              " ps -f status=running --format {{.Names}} 2>/dev/null"
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        containers = [x.strip('\r') for x in output.split('\n')]
        return containers

    def get_all_containers(self, host, filter_exprs=None):
        if filter_exprs:
            filter_cmd = ' | grep -v "%s" ' % '\|'.join(filter_exprs)
        else:
            filter_cmd = ''
        cmd = self.tool + ' ps -a 2>/dev/null ' + filter_cmd + \
                          ' | awk \'{print $NF}\''
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        containers = [x.strip('\r') for x in output.split('\n')]
        return containers

    def is_container_up(self, host, container_name):
        cmd = self.tool + " ps -f name=" + container_name + \
                          " -f status=running 2>/dev/null"
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        return 'Up' in output

    def action_on_service(self, host, event, service):
        issue_cmd = 'service %s %s' % (service, event)
        self.inputs.run_cmd_on_server(host, issue_cmd, pty=True, as_sudo=True, container=service)

    def action_on_container(self, host, event, container_name, timeout):
        timeout = '-t %s' % timeout if timeout else ''
        timeout = '' if event == 'start' else timeout
        cmd = self.tool + ' %s %s %s' % (event, container_name, timeout)
        self.inputs.run_cmd_on_server(host, cmd, pty=True, as_sudo=True)

    def copy_out(self, host, container_name, src_path, dst_path='.'):
        cmd = self.tool + ' cp %s:/%s %s' % (container_name, src_path,
                                            dst_path)
        self.inputs.run_cmd_on_server(host, cmd, pty=True, as_sudo=True)

    def copy_in(self, host, container_name, src_path, dst_path='/'):
        cmd = self.tool + ' cp %s %s:/%s' % (src_path, container_name,
                                             dst_path)
        self.inputs.run_cmd_on_server(host, cmd, pty=True, as_sudo=True)

    def recompose_services(self, host, yml_dir, yml_file=None):
        yml_file_str = '-f %s' % yml_file if yml_file else ''
        cmd = 'cd %s ; ' % yml_dir
        down_cmd = cmd + self.tool + '-compose %s down' % yml_file_str
        up_cmd = cmd + self.tool + '-compose %s up -d' % yml_file_str
        self.inputs.run_cmd_on_server(host, down_cmd, pty=True, as_sudo=True)
        self.inputs.run_cmd_on_server(host, up_cmd, pty=True, as_sudo=True)

    def run_cmd_on_container(self, cmd, host, container,
                             pty=True,
                             detach=None,
                             shell_prefix='/bin/bash -c '):
        cntr = self.inputs.host_data[host].get('containers', {}).get(container)
        args = ' -d ' if detach else ''
        args += ' --privileged '
        args += ' -it ' if pty else ''
        args += cntr
        cntr_cmd = self.tool + ' exec ' + args
        if shell_prefix:
            exec_cmd = '%s %s \'%s\'' % (cntr_cmd, shell_prefix, cmd)
        else:
            exec_cmd = '%s %s' % (cntr_cmd, cmd)
        return self.inputs.run_cmd_on_server(host, exec_cmd, pty=pty, as_sudo=True)


class PodmanWrapper(DockerWrapper):

    def __init__(self, inputs):
        self.inputs = inputs
        self.tool = 'podman'

class CtrWrapper:
    

    def __init__(self, inputs):
        self.inputs = inputs

    def get_active_containers(self, host):
        cmd = "ctr task ls | grep RUNNING | cut -f 1 -d ' ' "
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        containers = [x.strip('\r') for x in output.split('\n')]
        return containers

    def get_all_containers(self, host, filter_exprs=None):
        if filter_exprs:
            filter_cmd = ' | grep -v "%s" ' % '\|'.join(filter_exprs)
        else:
            filter_cmd = ''
        cmd = "ctr task ls | cut -f 1 -d ' ' " + filter_cmd
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        containers = [x.strip('\r') for x in output.split('\n')]
        return containers

    def is_container_up(self, host, container_name):
        cmd = "ctr task ls 2>/dev/null | grep RUNNING | grep " + container_name
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        return 'RUNNING' in output

    def action_on_container(self, host, event, container_name, timeout):
        timeout = '-t %s' % timeout if timeout else ''
        timeout = '' if event == 'start' else timeout
        cmd = 'systemctl' + ' %s %s' % (event, container_name)
        self.inputs.run_cmd_on_server(host, cmd, pty=True, as_sudo=True)

    def action_on_service(self, host, event, service):
        cmd = 'systemctl' + ' %s %s' % (event, service)
        self.inputs.run_cmd_on_server(host, cmd, pty=True, as_sudo=True)

    def copy_out(self, host, container_name, src_path, dst_path='.'):
        raise Exception('unimplemented')

    def copy_in(self, host, container_name, src_path, dst_path='/'):
        raise Exception('unimplemented')

    def recompose_services(self, host, yml_dir, yml_file=None):
        raise Exception('unimplemented')

    def run_cmd_on_container(self, cmd, host, container,
                             pty=True,
                             detach=None,
                             shell_prefix='/bin/bash -c '):
        cntr = self.inputs.host_data[host].get('containers', {}).get(container)
        cntr_cmd = 'ctr task exec '
        cntr_cmd += ' -d ' if detach else ''
        cntr_cmd += ' -t ' if pty else ''
        cntr_cmd += ' --exec-id %s ' % random.randint(10, 100)
        cntr_cmd += cntr
        if shell_prefix:
            exec_cmd = '%s %s \'%s\'' % (cntr_cmd, shell_prefix, cmd)
        else:
            exec_cmd = '%s %s' % (cntr_cmd, cmd)
        return self.inputs.run_cmd_on_server(host, exec_cmd, pty=pty, as_sudo=True)


def get_container_cli_wrapper(inputs):
    container_runtime = inputs.container_runtime

    import os
    if bool(os.getenv('RHOSP_16',False)) == True:
        container_runtime ='podman'
    
    if container_runtime == 'containerd':
        return CtrWrapper(inputs)
    elif container_runtime == 'podman':
        return PodmanWrapper(inputs)
    elif container_runtime == 'docker':
        return DockerWrapper(inputs)
    else:
        raise Exception('unsupported container container_runtime ' + container_runtime)
