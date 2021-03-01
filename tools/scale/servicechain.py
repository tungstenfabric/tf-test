import uuid
from vnc_api.vnc_api import *

class ServiceChain(object):
    def __init__(self, base_obj, user='admin', password='contrail123',
                 tenant='admin', api_server_host='10.204.216.64',
                 api_server_port='8082', auth_host='10.204.216.150', auth_token=None):
        self.obj = base_obj
        self.vnc = getattr(self.obj, 'vnc', None)
        if not self.vnc:
            self.vnc = VncApi(api_server_host=api_server_host,
                              api_server_port=api_server_port,
                              auth_host=auth_host,
                              tenant_name=tenant,
                              username=user,
                              password=password,
                              auth_token=auth_token)
            self.obj = self.vnc
            self.obj.project_obj = self.vnc.project_read(id=str(uuid.UUID(self.obj.tenant_id)))
    def create_svc_template(self, name, image_id, service_mode='in-network'):
         st_interfaces = [ServiceTemplateInterfaceType('left'),
                          ServiceTemplateInterfaceType('right')]
         st_prop = ServiceTemplateType(flavor='m1.tiny',
                                       image_name=image_id,
                                       ordered_interfaces=True,
                                       service_mode=service_mode,
                                       service_type='firewall',
                                       interface_type=st_interfaces)
         svc_template = ServiceTemplate(name=name,
                                        service_template_properties=st_prop)
         self.vnc.service_template_create(svc_template)
         self.obj.id.st_obj[name] = svc_template

    def create_svc_instance(self, name, st_name, left_vn_name, right_vn_name,
                            max_inst='1', auto_scale=True):
         st_obj = self.obj.id.st_obj[st_name]
         left_vn_obj = self.obj.id.vn_obj[left_vn_name]
         right_vn_obj = self.obj.id.vn_obj[right_vn_name]
         scale_out = ServiceScaleOutType(max_instances=int(max_inst),
                                         auto_scale=auto_scale)
         if_list = [ServiceInstanceInterfaceType(virtual_network=left_vn_obj.get_fq_name_str()),
                    ServiceInstanceInterfaceType(virtual_network=right_vn_obj.get_fq_name_str())]
         si_prop = ServiceInstanceType(auto_policy=True, interface_list=if_list, scale_out=scale_out)
         svc_instance = ServiceInstance(name=name, parent_obj=self.obj.project_obj, service_instance_properties=si_prop)
         svc_instance.add_service_template(st_obj)
         self.vnc.service_instance_create(svc_instance)
         self.obj.id.si_obj[name] = svc_instance

    def create_policy(self, name, src_vn, dst_vn, direction='<>',
                      protocol='any', si_name=None, n_rules=1):

        def _get_rule(src_vn, dst_vn, direction, protocol, min, max, action):
            src_addr = AddressType(virtual_network=src_vn)
            dst_addr = AddressType(virtual_network=dst_vn)
            return PolicyRuleType(rule_uuid=str(uuid.uuid4()),
                                  direction=direction,
                                  protocol=protocol, src_addresses=[src_addr],
                                  dst_addresses=[dst_addr],
                                  src_ports=[PortType(min, max)],
                                  dst_ports=[PortType(min, max)],
                                  action_list=action)
        
        rules = list()
        if si_name:
            si_fq_name = self.obj.id.si_obj[si_name].get_fq_name_str()
            action = ActionListType(apply_service=[si_fq_name])
        else:
            action = {'simple_action':'pass'}
        if src_vn in self.obj.id.vn_obj:
            src_vn_fq_name = self.obj.id.vn_obj[src_vn].get_fq_name_str()
            dst_vn_fq_name = self.obj.id.vn_obj[dst_vn].get_fq_name_str()
        else:
            src_vn_fq_name = ['default-domain', self.obj.project_obj.name, src_vn]
            dst_vn_fq_name = ['default-domain', self.obj.project_obj.name, dst_vn]
        for index in range(n_rules):
            rules.append(_get_rule(direction=direction, protocol=protocol,
                                   src_vn=src_vn_fq_name, dst_vn=dst_vn_fq_name,
                                   min=index-1, max=index, action=action))
        policy = NetworkPolicy(name, self.obj.project_obj, network_policy_entries=PolicyEntriesType(rules))
        self.obj.id.policy_id[name] = self.vnc.network_policy_create(policy)
        self.obj.update_network(src_vn, {'policys': [policy.fq_name]})
        self.obj.update_network(dst_vn, {'policys': [policy.fq_name]})
        self.obj.id.policy_obj[name] = policy

if __name__ == '__main__':
    svc = ServiceChain(None)
    svc.create_policy('policy1', src_vn="default-domain:admin:testvn", dst_vn="default-domain:admin:test-vn2")
