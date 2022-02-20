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

class PodmanWrapper(DockerWrapper):

    def __init__(self, inputs):
        self.inputs = inputs
        self.tool = 'podman'

class CtrWrapper:
    

    def __init__(self, inputs):
        self.inputs = inputs

    def get_active_containers(self, host):
        #TODO 
#        cmd = "ctr task ls 2>/dev/null | grep RUNNING"
        cmd = "ctr task ls | grep RUNNING | cut -f 1 -d ' ' "
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        containers = [x.strip('\r') for x in output.split('\n')]
        return containers

    def get_all_containers(self, host, filter_exprs=None):
        if filter_exprs:
            filter_cmd = ' | grep -v "%s" ' % '\|'.join(filter_exprs)
        else:
            filter_cmd = ''
        #TODO
#        cmd = "ctr task ls 2>/dev/null | cut -f 1 -d ' ' " + filter_cmd
        cmd = "ctr task ls | cut -f 1 -d ' ' " + filter_cmd
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        containers = [x.strip('\r') for x in output.split('\n')]
        return containers

    def is_container_up(self, host, container_name):
        #TODO
        cmd = "ctr task ls 2>/dev/null | grep RUNNING | grep " + container_name
        output = self.inputs.run_cmd_on_server(host, cmd, as_sudo=True)
        return 'RUNNING' in output

    def action_on_container(self, host, event, container_name, timeout):
        #TODO
        raise Exception('unimplemented')

    def copy_out(self, host, container_name, src_path, dst_path='.'):
        #TODO
        raise Exception('unimplemented')

    def copy_in(self, host, container_name, src_path, dst_path='/'):
        #TODO
        raise Exception('unimplemented')

    def recompose_services(self, host, yml_dir, yml_file=None):
        #TODO
        raise Exception('unimplemented')

def get_container_cli_wrapper(inputs):
    container_runtime = inputs.container_runtime

    #TODO: remove
    #set "contrail_cli: podman" under "test_configuration" input yaml. 
    #Set RHOSP_16 env to True for rhosp-16 deployments to use podman.
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
