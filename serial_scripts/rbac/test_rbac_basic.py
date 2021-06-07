from __future__ import absolute_import
from .base import BaseRbac
import os
import collections
import test
from tcutils.wrappers import preposttest_wrapper

class TestRbacBasic(BaseRbac):

    @test.attr(type=['sanity', 'suite1'])
    @preposttest_wrapper
    def test_rbac_acl_different_roles(self):
        '''
        Validate via vnc_apis CRUD of rbac acl and objects
        steps:
           1. Add user1 as role1 and user2 as role2 to the project
           2. Both user1 and user2 shouldnt be able to create VNs/STs
           3. Create Rbac ACL under project with VN.* role1:CRUD rule
           4. user1 should be able to create VN, but not Service-Template
           5. Create Rbac ACL under domain with ST.* role1:CRUD rule
           6. user1 should be able to create Service-Template
           7. user2 shouldnt be able to read the created VN/ST or create new
           8. Update the acl rule with Read perms for role2
           9. user2 should be able to read created VN but not create new VNs
           10. user2 should be able to read created ST but not create new STs
           11. Delete the acl rule with Read perms for role2
           12. user2 shouldnt be able to read the created ST/VN or create new VN/ST
           13. Update global acl with role2:R for both VN and ST
           14. user2 should be able to read VN and ST
           13. Delete both project and domain acls
           14. user1 shouldnt be able to read/delete VN/ST
           15. Update global acl with role1:CRUD for both VN/ST
           16. user1 should now be able to delete both VN and ST
           17. Delete global acl
        pass : acl creation and update should complete scucessfully.
        '''
        self.add_user_to_project(self.user1, self.role1)
        self.add_user_to_project(self.user2, self.role2)
        user1_conn = self.get_connections(self.user1, self.pass1)
        user2_conn = self.get_connections(self.user2, self.pass2)
        assert not self.create_vn(connections=user1_conn), 'VN creation should have failed'
        assert not self.create_st(connections=user1_conn), 'ST creation should have failed'
        vn_rules = [{'rule_object': 'virtual-network',
                     'rule_field': None,
                     'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                    },
                    ]
        proj_rbac = self.create_rbac_acl(rules=vn_rules)
        vn = self.create_vn(connections=user1_conn)
        assert vn, 'VN creation failed'
        assert not self.create_st(connections=user1_conn), 'ST creation should have failed'
        st_rules = [{'rule_object': 'service-template',
                     'rule_field': None,
                     'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                    },
                    ]
        domain_rbac = self.create_rbac_acl(rules=st_rules, parent_type='domain')
        st = self.create_st(connections=user1_conn)
        assert st, 'ST creation failed'
        assert not self.read_vn(connections=user2_conn, uuid=vn.uuid)
        assert not self.read_st(connections=user2_conn, uuid=st.uuid)
        if self.rbac_for_analytics:
            assert not self.get_vn_from_analytics(user2_conn, vn.vn_fq_name)
            assert vn.vn_fq_name not in self.list_vn_from_analytics(user2_conn)
        vn2_rules = [{'rule_object': 'virtual-network',
                      'rule_field': None,
                      'perms': [{'role': self.role2, 'crud': 'R'}]
                     },
                     ]
        proj_rbac.add_rules(vn2_rules)
        proj_rbac.verify_on_setup()
        assert self.read_vn(connections=user2_conn, uuid=vn.uuid)
        assert not self.create_vn(connections=user2_conn)
        assert not self.read_st(connections=user2_conn, uuid=st.uuid)
        if self.rbac_for_analytics:
            assert self.get_vn_from_analytics(user2_conn, vn.vn_fq_name)
            assert vn.vn_fq_name in self.list_vn_from_analytics(user2_conn)
        st2_rules = [{'rule_object': 'service-template',
                      'rule_field': None,
                      'perms': [{'role': self.role2, 'crud': 'R'}]
                     },
                     ]
        domain_rbac.add_rules(st2_rules)
        domain_rbac.verify_on_setup()
        assert self.read_st(connections=user2_conn, uuid=st.uuid)
        assert not self.create_st(connections=user2_conn)
        proj_rbac.delete_rules(vn2_rules)
        proj_rbac.verify_on_setup()
        domain_rbac.delete_rules(st2_rules)
        domain_rbac.verify_on_setup()
        assert not self.read_vn(connections=user2_conn, uuid=vn.uuid)
        assert not self.read_st(connections=user2_conn, uuid=st.uuid)
        if self.rbac_for_analytics:
            assert not self.get_vn_from_analytics(user2_conn, vn.vn_fq_name)
            assert vn.vn_fq_name not in self.list_vn_from_analytics(user2_conn)
        self.global_acl.add_rules(rules=vn2_rules+st2_rules)
        self._cleanups.insert(0, (self.global_acl.delete_rules, (), {'rules': vn2_rules+st2_rules}))
        assert self.read_st(connections=user2_conn, uuid=st.uuid)
        assert self.read_vn(connections=user2_conn, uuid=vn.uuid)
        if self.rbac_for_analytics:
            assert self.get_vn_from_analytics(user2_conn, vn.vn_fq_name)
            assert vn.vn_fq_name in self.list_vn_from_analytics(user2_conn)
        proj_rbac.cleanUp(); self.remove_from_cleanups(proj_rbac)
        domain_rbac.cleanUp(); self.remove_from_cleanups(domain_rbac)
        assert not self.read_vn(connections=user1_conn, uuid=vn.uuid)
        assert not self.read_st(connections=user1_conn, uuid=st.uuid)
        if self.rbac_for_analytics:
            assert not self.get_vn_from_analytics(user1_conn, vn.vn_fq_name)
            assert vn.vn_fq_name not in self.list_vn_from_analytics(user1_conn)
        self.global_acl.add_rules(rules=vn_rules+st_rules)
        self._cleanups.insert(0, (self.global_acl.delete_rules, (), {'rules': vn_rules+st_rules}))
        assert self.read_vn(connections=user1_conn, uuid=vn.uuid)
        assert self.read_st(connections=user1_conn, uuid=st.uuid)
        if self.rbac_for_analytics:
            assert self.get_vn_from_analytics(user1_conn, vn.vn_fq_name)
            assert vn.vn_fq_name in self.list_vn_from_analytics(user1_conn)
        return True

    @test.attr(type=['sanity', 'suite1'])
    @preposttest_wrapper
    def test_rbac_create_delete_vm(self):
        '''
        Validate creds passed via orchestrator(nova/neutron)
        steps:
           1. Add user1 as role1
           2. Create Rbac ACL under project with role1:CRUD perms for
                a. VN.*
                b. VM.*
                c. VMI.*
                d. IIP.*
                e. SG.*
                f. LR.*
                g. FIP-Pool.*
                h. ACL.*
           3. user1 should be able to create VN and VM via orchestrator
           4. Validate the VN and VM
        pass: user should be able to create and delete VN and VM
        '''
        pub_vn = self.create_vn(option='quantum', router_external=True, shared=True)
        self.add_user_to_project(self.user1, self.role1)
        user1_conn = self.get_connections(self.user1, self.pass1)
        rules = [{'rule_object': 'virtual-network',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                 },
                 {'rule_object': 'floating-ip-pool',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                 },
                 {'rule_object': 'floating-ip',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                 },
                 {'rule_object': 'virtual-machine',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                 },
                 {'rule_object': 'virtual-machine-interface',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                 },
                 {'rule_object': 'instance-ip',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                 },
                 {'rule_object': 'security-group',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                 },
                 {'rule_object': 'logical-router',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'R'}]
                 },
                 {'rule_object': 'access-control-list',
                  'rule_field': None,
                  'perms': [{'role': self.role1, 'crud': 'R'}]
                 },
                 ]
        proj_rbac = self.create_rbac_acl(rules=rules)
        vn = self.create_vn(connections=user1_conn, option='neutron')
        assert vn, 'VN creation failed'
        sg = self.create_sg(connections=user1_conn)
        assert sg, 'SG creation failed'
        vm = self.create_vm(connections=user1_conn, vn_fixture=vn)
        assert vm, 'VM creation failed'
        fip_pool = self.create_fip_pool(pub_vn, connections=user1_conn,
                                        verify=False)
        (fip, fip_id) = self.create_fip(connections=user1_conn,
                        fip_pool=fip_pool, vm_fixture=vm, pub_vn_fixture=pub_vn)
        assert fip and fip_id, "fip creation failed"
        if self.rbac_for_analytics:
            assert self.get_vn_from_analytics(user1_conn, vn.vn_fq_name)
            assert vn.vn_fq_name in self.list_vn_from_analytics(user1_conn)
        self.associate_sg(sg, vm)

    @test.attr(type=['sanity', 'suite1'])
    @preposttest_wrapper
    def test_perms2_owner(self):
        '''
        Validate perms2 tenant ownership
        steps:
            1. Create Project1 and Project2
            2. Add user1 as role1 under project1 and project2
            3. create domain acl rule 'VirtualNetwork.* role1:CRUD'
            4. create VN1 under Project1
            4. create VN2 under Project2
            5. user1 shouldnt be able to read VN1 using project2 creds
            6. admin should be able to read VN1 though he isnt member of the project
            7. Network list with respective project creds should list corresponding VNs
            8. Change ownership of VN1 to Project2
            9. user1 should now be able to read VN1 using Project2 creds
            10. Network list with Project2 creds should list both VNs,
                Project1 creds should list VN1 alone, admin should list both VNs
        '''
        project1 = self.create_project()
        project2 = self.create_project()
        self.add_user_to_project(self.user1, self.role1, project1.project_name)
        self.add_user_to_project(self.user1, self.role1, project2.project_name)
        u1_p1_conn = self.get_connections(self.user1, self.pass1, project1)
        u1_p2_conn = self.get_connections(self.user1, self.pass1, project2)
        vn_rules = [{'rule_object': 'virtual-network',
                     'rule_field': None,
                     'perms': [{'role': self.role1, 'crud': 'CRUD'}]
                    },
                    ]
        domain_rbac = self.create_rbac_acl(rules=vn_rules, parent_type='domain')
        vn = self.create_vn(connections=u1_p1_conn, verify=False)
        assert vn, 'VN creation failed'
        vn2 = self.create_vn(connections=u1_p2_conn, verify=False)
        assert vn2, 'VN creation failed'
        assert self.read_vn(connections=u1_p1_conn, uuid=vn.uuid)
        assert not self.read_vn(connections=u1_p2_conn, uuid=vn.uuid)
        assert self.read_vn(connections=self.connections, uuid=vn.uuid)
        vns = self.list_vn(connections=u1_p1_conn)
        assert (vn.uuid in vns) and (not vn2.uuid in vns)
        vns = self.list_vn(connections=u1_p2_conn)
        assert (vn2.uuid in vns) and (not vn.uuid in vns)
        if self.rbac_for_analytics:
            assert self.get_vn_from_analytics(u1_p1_conn, vn.vn_fq_name)
            assert not self.get_vn_from_analytics(u1_p2_conn, vn.vn_fq_name)
            assert self.get_vn_from_analytics(self.connections, vn.vn_fq_name)
            vns = self.list_vn_from_analytics(u1_p1_conn)
            assert vn.vn_fq_name in vns and vn2.vn_fq_name not in vns
            vns = self.list_vn_from_analytics(u1_p2_conn)
            assert vn.vn_fq_name not in vns and vn2.vn_fq_name in vns
            vns = self.list_vn_from_analytics(self.connections)
            assert vn.vn_fq_name in vns and vn2.vn_fq_name in vns
        self.set_owner(vn.api_vn_obj, project2)
        self._cleanups.append((self.set_owner, (vn.api_vn_obj, project1), {}))
        vns = self.list_vn(connections=u1_p1_conn)
        assert not (vn.uuid in vns or vn2.uuid in vns)
        vns = self.list_vn(connections=u1_p2_conn)
        assert (vn2.uuid in vns) and (vn.uuid in vns)
        vns = self.list_vn()
        assert (vn2.uuid in vns) and (vn.uuid in vns)
        if self.rbac_for_analytics:
            assert not self.get_vn_from_analytics(u1_p1_conn, vn.vn_fq_name)
            assert self.get_vn_from_analytics(u1_p2_conn, vn.vn_fq_name)
            assert self.get_vn_from_analytics(self.connections, vn.vn_fq_name)
            vns = self.list_vn_from_analytics(u1_p1_conn)
            assert vn.vn_fq_name not in vns and vn2.vn_fq_name not in vns
            vns = self.list_vn_from_analytics(u1_p2_conn)
            assert vn.vn_fq_name in vns and vn2.vn_fq_name in vns
            vns = self.list_vn_from_analytics(self.connections)
            assert vn.vn_fq_name in vns and vn2.vn_fq_name in vns

    def vn_create_map(self, vn_perm):
        return self.create_vn(project_name=vn_perm[0], option='contrail',
                              shared=vn_perm[1], router_external=vn_perm[2],
                              verify=False, connections=vn_perm[3])

    def verify_vn_listing(self, v_inp):
        connection=v_inp['con'] or self.connections
        flag=v_inp['flag']
        vn_l=v_inp['vns']
        fetch_list=[]
        if flag == 'shared':
            fetch_list=[vn['name'] for vn in \
                        connection.orch.quantum_h.list_networks(shared=True)]
        elif flag == 'non-shared':
            fetch_list=[vn['name'] for vn in \
                        connection.orch.quantum_h.list_networks(shared=False)]
        else:
            fetch_list=[vn['name'] for vn in \
                        connection.orch.quantum_h.list_networks()]

        if v_inp['con'] is None:
            if((set(vn_l) & set(fetch_list)) == set(vn_l)):
                return True
        elif collections.Counter(vn_l) == collections.Counter(fetch_list):
            return True
        else:
            msg='VN listing for %s Failed!!!' %connection.username \
                if flag is None else 'VN listing for %s flag, %s \
                User Failed!!!' %(flag, connection.username)
            assert False, msg

    @preposttest_wrapper
    def test_vn_share_external_flag_with_member_role(self):
        '''
        Verify CEM-20393 and CEM-21693 (Once fixed).
            Steps:-
            1. Create 2 Projects tp1 and tp2.
            2. Create 2 Users tu1 and tu2.
            3. Add tu1 with _member_ role to tp1.
            4. Add tu2 with _member_ role to tp2.
            5. Create VN's in tp1 and tp2.
               in tp1:       SHARED       EXTERNEL
                   vn11        0             0
                   vn12        0             1
                   vn13        1             0
                   vn14        1             1

               in tp2:       SHARED       EXTERNEL
                   vn21        0             0
                   vn22        0             1
                   vn23        1             0
                   vn24        1             1
            6. Create Rbac ACL VN.* _member_:CRUD rule.

            Verify:-
            1. admin VN List                     - vn11-vn14,vn21-vn24
            2. admin VN List shared              - vn13,vn14,vn23,vn24
            3. admin VN List non-shared          - vn11,vn12,vn21,vn22
            4. admin VN List external            - vn12,vn14,vn22,vn24
            5. admin VN List internal            - vn11,vn13,vn21,vn23
            6. admin VN List shared external     - vn14,vn24
            7. admin VN List shared internal     - vn13,vn23
            8. admin VN List non-shared external - vn12,vn22
            9. admin VN List non-shared internal - vn11,vn21

            with tu1 creds:
            1. tu1 VN List                       - vn11-vn14,vn23,vn24
            2. tu1 VN List shared                - vn13,vn14,vn23,vn24
            3. tu1 VN List non-shared            - vn11,vn12
            4. tu1 VN List external              - vn12,vn14,vn24
            5. tu1 VN List internal              - vn11,vn13,vn23
            6. tu1 VN List shared external       - vn14,vn24
            7. tu1 VN List shared internal       - vn13,vn23
            8. tu1 VN List non-shared external   - vn12
            9. tu1 VN List non-shared internal   - vn11

            with tu2 creds:
            1. tu2 VN List                       - vn13,vn14,vn21-vn24
            2. tu2 VN List shared                - vn13,vn14,vn23,vn24
            3. tu2 VN List non-shared            - vn21,vn22
            4. tu2 VN List external              - vn14,vn22,vn24
            5. tu2 VN List internal              - vn13,vn21,vn23
            6. tu2 VN List shared external       - vn14,vn24
            7. tu2 VN List shared internal       - vn13,vn23
            8. tu2 VN List non-shared external   - vn22
            9. tu2 VN List non-shared internal   - vn21

        '''
        vn_rules = [{'rule_object': 'virtual-network',
                     'rule_field': '*',
                     'perms': [{'role': '_member_', 'crud': 'CRUD'}]}]
        rbac = self.global_acl.add_rules(rules=vn_rules)
        self._cleanups.insert(0, (self.global_acl.delete_rules, (),
                                 {'rules': vn_rules}))
        tp1=self.create_project()
        tp2=self.create_project()
        self.admin_connections.auth.create_user('tu1', 'tu1passwd')
        self.admin_connections.auth.create_user('tu2', 'tu2passwd')
        self.add_user_to_project(username=self.connections.username,
                                 role='admin', project_name=tp1.project_name)
        self.add_user_to_project(username=self.connections.username,
                                 role='admin', project_name=tp2.project_name)
        self.add_user_to_project(username='tu1', role='_member_',
                                 project_name=tp1.project_name)
        self.add_user_to_project(username='tu2', role='_member_',
                                 project_name=tp2.project_name)
        tu1_con=self.get_connections(username='tu1', password='tu1passwd',
                                     project_fixture=tp1)
        tu2_con=self.get_connections(username='tu2', password='tu2passwd',
                                     project_fixture=tp2)

        #         Project            Share  Externel Connections
        vn_perms=([tp1.project_name, False, False,   tu1_con],
                  [tp1.project_name, False, True,    tu1_con],
                  [tp1.project_name, True,  False,   tu1_con],
                  [tp1.project_name, True,  True,    tu1_con],
                  [tp2.project_name, False, False,   tu2_con],
                  [tp2.project_name, False, True,    tu2_con],
                  [tp2.project_name, True,  False,   tu2_con],
                  [tp2.project_name, True,  True,    tu2_con],)

        vn_list=list(map(self.vn_create_map, vn_perms))

        verification=({'con' : None, 'flag' : None,
                       'vns' : [vn_list[0].vn_name, vn_list[1].vn_name,
                                vn_list[2].vn_name, vn_list[3].vn_name,
                                vn_list[4].vn_name, vn_list[5].vn_name,
                                vn_list[6].vn_name, vn_list[7].vn_name]}, #admin vns
                      {'con' : None, 'flag' : 'shared',
                       'vns' : [vn_list[2].vn_name, vn_list[3].vn_name,
                                vn_list[6].vn_name, vn_list[7].vn_name]}, #admin shared vns
                      {'con' : None, 'flag' : 'non-shared',
                       'vns' : [vn_list[0].vn_name, vn_list[1].vn_name,
                                vn_list[4].vn_name, vn_list[5].vn_name]}, #admin non-shared vns
                      {'con' : tu1_con, 'flag' : None,
                       'vns' : [vn_list[0].vn_name, vn_list[1].vn_name,
                                vn_list[2].vn_name, vn_list[3].vn_name,
                                vn_list[6].vn_name, vn_list[7].vn_name]}, #tu1 vns
                      {'con' : tu1_con, 'flag' : 'shared',
                       'vns' : [vn_list[2].vn_name, vn_list[3].vn_name,
                                vn_list[6].vn_name, vn_list[7].vn_name]}, #tu1 shared vns
                      {'con' : tu1_con, 'flag' : 'non-shared',
                       'vns' : [vn_list[0].vn_name, vn_list[1].vn_name]}, #tu1 non-shared vns
                      {'con' : tu2_con, 'flag' : None,
                       'vns' : [vn_list[2].vn_name, vn_list[3].vn_name,
                                vn_list[4].vn_name, vn_list[5].vn_name,
                                vn_list[6].vn_name, vn_list[7].vn_name]}, #tu2 vns
                      {'con' : tu2_con, 'flag' : 'shared',
                       'vns' : [vn_list[2].vn_name, vn_list[3].vn_name,
                                vn_list[6].vn_name, vn_list[7].vn_name]}, #tu2 shared vns
                      {'con' : tu2_con, 'flag' : 'non-shared',
                       'vns' : [vn_list[4].vn_name, vn_list[5].vn_name]}) #tu2 non-shared vns

        vn_list_verify=list(map(self.verify_vn_listing, verification))

        return True
    #end test_vn_share_external_flag_with_member_role
