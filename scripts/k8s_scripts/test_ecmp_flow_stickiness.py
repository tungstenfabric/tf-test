from common.k8s.base import BaseK8sTest
from builtins import range
from tcutils.util import skip_because
from k8s.namespace import NamespaceFixture
from k8s.service import ServiceFixture
from tcutils.wrappers import preposttest_wrapper
from tcutils.util import get_lock
import test
from tcutils.util import get_random_name
import time
import unittest

class TestEcmpFlowStickiness(BaseK8sTest):

    @classmethod
    def setUpClass(cls):
        super(TestEcmpFlowStickiness, cls).setUpClass()
        if cls.inputs.compute_control_ips:
          cls.cn_list = list(cls.inputs.compute_control_ips)
        else:
          cls.cn_list = list(cls.inputs.compute_ips)
        assert cls._connections.k8s_client.set_label_for_hbf_nodes( \
            node_selector='computenode'), "Error : could not label the nodes"

    @classmethod
    def tearDownClass(cls):
        super(TestEcmpFlowStickiness, cls).tearDownClass()
        assert cls._connections.k8s_client.set_label_for_hbf_nodes( \
              labels={"type":None}), "Error : could not label the nodes"

    def parallel_cleanup(self):
        parallelCleanupCandidates = ["PodFixture"]
        self.delete_in_parallel(parallelCleanupCandidates)

    @preposttest_wrapper
    def test_ecmp_local_scale_up_down(self):
        ''' Create a service with 3 pods in worker_node_1
            Create a client pod in worker_node_1 which will scp a file.
            Scale up/down and verify that scp should not fail.
            Verify that ecmp index and flow index should not change after scale up.
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels)
        # create client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name,
                compute_node_selector= compute_selector_1)
        assert client_pod.verify_on_setup()

        # create webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert service.verify_on_setup()

        assert self.validate_scp(client_pod, service.cluster_ip)
        self.logger.info("Scp connection is working")

        self.do_scp(client_pod, service.cluster_ip, limit_rate=True)

        assert self.validate_ssh(client_pod)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)

        ecmp_index = self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        flow_index = self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        # scale up and verify that scp doesn't fail
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        pod4 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        pod5= self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        assert pod3.verify_on_setup()
        assert pod4.verify_on_setup()
        assert pod5.verify_on_setup()
        # ecmp_index and flow_index should not change
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        assert flow_index == self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        assert self.validate_ssh(client_pod)
        self.logger.info("Scp connection is not broken")

        # delete a pod and verify that scp should not fail
        pod4.delete()
        assert self.validate_ssh(client_pod)
        self.logger.info("Scp connection is not broken")
        # ecmp_index and flow_index should not change
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        self.logger.info("test_ecmp_local_scale_up_down passed")
    # end test_ecmp_local_scale_up_down

    @preposttest_wrapper
    def test_ecmp_remote_scale_up_down(self):
        ''' Create a service with 3 pods in worker_node_2
            Create a client pod in worker_node_1 which will scp a file.
            Scale up/down and verify that scp should not fail.
            Verify that ecmp index and flow index should not change after scale up.
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels)
        # create scp client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name, \
                compute_node_selector= compute_selector_1)
        assert client_pod.verify_on_setup()

        # create ssh webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert service.verify_on_setup()

        assert self.validate_scp(client_pod, service.cluster_ip)

        self.do_scp(client_pod, service.cluster_ip, limit_rate=True)
        assert self.validate_ssh(client_pod)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)

        ecmp_index = self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        flow_index = self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        # scale up and verify that scp doesn't fail
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod4 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod5= self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod4.verify_on_setup()
        assert pod3.verify_on_setup()
        assert pod5.verify_on_setup()
        assert self.validate_ssh(client_pod)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        # ecmp_index and flow_index should not change
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        assert flow_index == self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        self.logger.info("Scp connection is not broken")

        # delete a pod and verify that scp should not fail
        pod4.delete()
        assert self.validate_ssh(client_pod)
        self.logger.info("Scp connection is not broken")
        self.logger.info("test_ecmp_remote_scale_up_down passed")
    # end test_ecmp_remote_scale_up_down

    @preposttest_wrapper
    def test_ecmp_remote_nodeport_service(self):
        ''' Create a nodeport service with 3 pods in worker_node_2
            Create a client pod in worker_node_1 which will scp a file.
            Scale up/down and verify that scp should not fail.
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        app = 'scp_nodeport_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels, type="NodePort")
        # create ssh webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels)
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert pod3.verify_on_setup()
        assert service.verify_on_setup()

        # validate Service Nodeport functionality
        for compute in self.cn_list:
            self.do_scp(None, compute, port=service.nodePort, limit_rate=True)
            assert self.validate_ssh()

        pod4 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels)
        pod5 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels)
        assert pod4.verify_on_setup()
        assert pod5.verify_on_setup()

        for compute in self.cn_list:
            assert self.validate_ssh()
        self.logger.info("Scp connection is not broken")

        # scale down and verify scp is working
        self.logger.info("Scaling down pods")
        pod4.delete()

        for compute in self.cn_list:
            assert self.validate_ssh()
        self.logger.info("Scp connection is not broken")
        self.logger.info("test_ecmp_remote_nodeport_service passed")
    # end test_ecmp_remote_nodeport_service

    @preposttest_wrapper
    def test_ecmp_remote_scale_up_down_multiple_clients(self):
        ''' Create a service with 3 pods in worker_node_2
            Create 2 client pods in worker_node_1 which will scp a file.
            Scale up/down and verify that scp should not fail.
            Verify that flow index and ecmp index should not change
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels)
        # create scp client pod
        client_pod1 = self.setup_ssh_client_pod(namespace=namespace.name, \
                compute_node_selector= compute_selector_1)
        client_pod2 = self.setup_ssh_client_pod(namespace=namespace.name, \
                compute_node_selector= compute_selector_1)
        assert client_pod1.verify_on_setup()
        assert client_pod2.verify_on_setup()

        # create ssh webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert service.verify_on_setup()

        assert self.validate_scp(client_pod1, service.cluster_ip)
        assert self.validate_scp(client_pod2, service.cluster_ip)

        # do scp from both clients, scale up, scp should not break.
        self.do_scp(client_pod2, service.cluster_ip, limit_rate=True)
        self.do_scp(client_pod1, service.cluster_ip, limit_rate=True)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod1.pod_ip)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)

        ecmp_index1 = self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod1.pod_ip)
        ecmp_index2 = self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        flow_index1 = self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod1.pod_ip)
        flow_index2 = self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod4 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod5 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod3.verify_on_setup()
        assert pod4.verify_on_setup()
        assert pod5.verify_on_setup()

        # check if scp is running
        assert self.validate_ssh(client_pod1)
        assert self.validate_ssh(client_pod2)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod1.pod_ip)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        assert ecmp_index1 == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod1.pod_ip)
        assert ecmp_index2 == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        assert flow_index1 == self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod1.pod_ip)
        assert flow_index2 == self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        self.logger.info("Scp connections are not broken")
        self.logger.info("test_ecmp_remote_scale_up_down_multiple_clients passed")
    # end test_ecmp_remote_scale_up_down_multiple_clients

    @skip_because(mx_gw = False)
    @preposttest_wrapper
    def test_ecmp_remote_scale_up_down_external_ip(self):
        ''' Create a service with 3 pods in worker_node_2
            Create 2 client pods in worker_node_1 which will scp a file.
            Use service's external ip to scp file.
            Scale up/down and verify that scp should not fail.
            Verify that ecmp index and flow index should not change after scale up.
        '''
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1

        pub_vn_fixture = self.public_vn.public_vn_fixture
        with get_lock(self.inputs.fip_pool):
            external_ips = pub_vn_fixture.alloc_ips(1)
            assert external_ips, 'No free IP available to use in public VN'
            pub_vn_fixture.free_ips(external_ips)
            service = self.setup_ssh_service(namespace=namespace.name,
                                              labels=labels,
                                              external_ips=external_ips)
            assert service.verify_on_setup()

        # create ssh webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_1)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_1)
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod4 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert pod3.verify_on_setup()
        assert pod4.verify_on_setup()

        assert self.validate_scp(None, service.external_ips[0])

        # do scp from both clients, scale up, scp should not break.
        self.do_scp(None, service.external_ips[0], limit_rate=True)
        assert self.validate_ssh(None, True)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.external_ips[0], self.inputs.k8s_master_ip)
        assert self.get_ecmp_index(self.inputs.compute_ips,
                                service.external_ips[0], self.inputs.k8s_master_ip)
        assert self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.external_ips[0], self.inputs.k8s_master_ip)
        pod5 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_1)
        pod6 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        # check if scp is running
        assert self.validate_ssh(None, True)
        self.logger.info("Scp connections are not broken")
        self.logger.info("test_ecmp_remote_scale_up_down_external_ip passed")
    # end test_ecmp_remote_scale_up_down_external_ip

    @preposttest_wrapper
    def test_ecmp_remote_scale_up_to_10_and_down_to_2(self):
        ''' Create a service with 2 pods in worker_node_2
            Create a client pod in worker_node_1 which will scp a file.
            Scale up/down and verify that scp should not fail.
            Verify that ecmp index and flow index should not change after scale up.
        '''
        all_pods = []
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels)
        assert service.verify_on_setup()

        # create scp client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name, \
                compute_node_selector= compute_selector_1)
        assert client_pod.verify_on_setup()

        # create 2 ssh webserver pod
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod1.verify_on_setup()
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod2.verify_on_setup()

        assert self.validate_scp(client_pod, service.cluster_ip)

        self.do_scp(client_pod, service.cluster_ip, limit_rate=True)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)

        ecmp_index = self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        flow_index = self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)

        # scale up to 10 pods and verify that scp is working
        assert self.validate_ssh(client_pod)
        for i in range(0, 8):
            pod = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                    labels=labels, compute_node_selector=compute_selector_2)
            all_pods.append(pod)
        # end for

        for pod in all_pods:
            assert pod.verify_on_setup()

        # check scp is running
        assert self.validate_ssh(client_pod)
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        assert flow_index == self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)

        # Scale down to 2 pods(delete newly added pods). Scp should not fail
        for pod in all_pods:
            pod.delete()

        # check scp is running
        assert self.validate_ssh(client_pod)
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        self.logger.info("test_ecmp_remote_scale_up_to_10_and_down_to_2 passed")
    # end test_ecmp_remote_scale_up_to_10_and_down_to_2

    @unittest.skip("Enable when openshift setup is stable")
    @preposttest_wrapper
    def test_ecmp_flow_stickiness_restart_agent(self):
        ''' Create a service with 3 pods in worker_node_2
            Create a client pod in worker_node_1 which will scp a file.
            Restart agent will stop scp, once agent is up again,
            run scp command again and it should work.
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels, type='LoadBalancer')
        # create scp client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name, \
                compute_node_selector= compute_selector_1)
        assert client_pod.verify_on_setup()

        # create ssh webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert pod3.verify_on_setup()
        assert service.verify_on_setup()

        # check if scp is running
        assert self.validate_scp(client_pod, service.cluster_ip)

        # restart agent and check that scp is working
        self.restart_vrouter_agent()
        self.restart_contrail_control()

        # check if scp is running
        assert self.validate_scp(client_pod, service.cluster_ip)
        self.logger.info("test_ecmp_flow_stickiness_restart_agent passed")
    # end test_ecmp_flow_stickiness_restart_agent

    @unittest.skip("Enable when openshift setup is stable")
    @preposttest_wrapper
    def test_ecmp_flow_stickiness_restart_control(self):
        ''' Create a service with 3 pods in worker_node_2
            Create a client pod in worker_node_1 which will scp a file.
            Restart contrail-control will stop scp, once service is up again,
            run scp command again and it should work.
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels, type='LoadBalancer')
        # create scp client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name, \
                compute_node_selector= compute_selector_1)
        assert client_pod.verify_on_setup()

        # create ssh webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert pod3.verify_on_setup()
        assert service.verify_on_setup()

        # check if scp is running
        assert self.validate_scp(client_pod, service.cluster_ip)

        # restart contrail-control and check that scp is working
        self.restart_contrail_control()

        # check if scp is running
        assert self.validate_scp(client_pod, service.cluster_ip)
        self.logger.info("test_ecmp_flow_stickiness_restart_control passed")
    # end test_ecmp_flow_stickiness_restart_control

    @preposttest_wrapper
    def test_ecmp_remote_network_policy(self):
        '''
        Create a service with 4 pods
        Create 2 client pods
        Create a network policy which will allow ingress traffic from only
        one client pod.
        Do scp/ssh from both clients, only one pod will succeed
        Scale up/down and verify that scp/ssh does not fail
        Ecmp and flow index should not change during scale up/down
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1
        app = 'webserver'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels)
        # create client pods
        client_pod1 = self.setup_ssh_client_pod(namespace=namespace.name, \
                labels={'app': 'client1'}, \
                compute_node_selector= compute_selector_1)
        client_pod2 = self.setup_ssh_client_pod(namespace=namespace.name, \
                labels={'app': 'client2'}, \
                compute_node_selector= compute_selector_1)
        assert client_pod1.verify_on_setup()
        assert client_pod2.verify_on_setup()

        # Create a network policy with ingress rules such that ingress traffic
        # to nginx pod from client2 is only allowed.
        # Verify an ingress policy
        policy_types = ["Ingress"]
        ingress_list = [
            {'from': [
                {'pod_selector': {'app': 'client2'}},
                    ]
             }
        ]
        policy = self.setup_update_policy(pod_selector={'app': 'webserver'},
                name="ingress-policy-over-project-ns",
                namespace=namespace.name,
                policy_types=policy_types,
                ingress=ingress_list)
        assert policy.verify_on_setup()

        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_1)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_1)
        pod3 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        pod4 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert pod3.verify_on_setup()
        assert pod4.verify_on_setup()
        assert service.verify_on_setup()

        # scp/ssh should not work from client1 because of network-policy
        assert self.validate_scp(client_pod1, service.cluster_ip, False)

        # scp/ssh should work from client2 because of network-policy
        assert self.validate_scp(client_pod2, service.cluster_ip)
        self.do_scp(client_pod2, service.cluster_ip, limit_rate=True)
        assert self.validate_ssh(client_pod2)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)

        ecmp_index = self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        flow_index = self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)

        # scale up pods and check that scp/ssh doesn't fail
        # ecmp index and flow index should not change
        pod5 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_1)
        pod6 = self.setup_ssh_webserver_pod(namespace=namespace.name, \
                labels=labels, compute_node_selector=compute_selector_2)
        assert pod5.verify_on_setup()
        assert pod6.verify_on_setup()

        assert self.validate_ssh(client_pod2)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        # ecmp_index and flow_index should not change
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        assert flow_index == self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)

        # delete pods and verify that scp should not fail
        pod5.delete()
        pod6.delete()
        assert self.validate_ssh(client_pod2)
        self.logger.info("Scp connection is not broken")
        # ecmp_index and flow_index should not change
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod2.pod_ip)
        self.logger.info("test_ecmp_remote_network_policy passed")
    #end test_ecmp_remote_network_policy

    @preposttest_wrapper
    def test_ecmp_flow_stickiness_with_deployment(self):
        '''
        Create a deployment with n replicas.
        Update the deployment to have more replicas.
        Validate that a service with expected replicas work.
        Verify that flow index and ecmp index should not change.
        '''
        labels = {'a': 'b'}
        replicas = len(self.inputs.compute_ips)*2
        new_replicas = len(self.inputs.compute_ips)*3
        namespace = self.setup_namespace()

        # create client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name)
        assert client_pod.verify_on_setup()
        dep_1 = self.setup_ssh_webserver_deployment(namespace=namespace.name,
            replicas=replicas, pod_labels=labels)
        assert dep_1.verify_on_setup()
        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels, type='LoadBalancer')
        self.validate_scp(client_pod, service.cluster_ip)
        # do scp, scale up and verify that scp doesn't fail
        self.do_scp(client_pod, service.cluster_ip, limit_rate=True)
        assert self.validate_ssh(client_pod)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        ecmp_index = self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        flow_index = self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        self.logger.info("Scp connection is not broken")
        # scale up deployment
        dep_1.set_replicas(new_replicas)
        assert dep_1.verify_on_setup()
        assert self.validate_ssh(client_pod)
        assert ecmp_index == self.get_ecmp_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        assert flow_index == self.get_ecmp_flow_index(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        self.logger.info("Scp connection is not broken")
        self.logger.info("test_ecmp_flow_stickiness_with_deployment passed")
    # end test_ecmp_flow_stickiness_with_deployment

    @preposttest_wrapper
    def test_non_ecmp_to_ecmp(self):
        ''' Create a service with 1 pods in worker_node_2
            Create a client pod in worker_node_1 which will scp a file.
            Ecmp index should not be present in flow.
            Scale up to 3 pods and do scp again, flow should have ecmp index.
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels)
        # create client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name,
                compute_node_selector= compute_selector_1)
        assert client_pod.verify_on_setup()

        # create webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        assert pod1.verify_on_setup()
        assert service.verify_on_setup()

        assert self.validate_scp(client_pod, service.cluster_ip)

        # do scp and check that the flow does not have ecmp index
        self.do_scp(client_pod, service.cluster_ip, limit_rate=True)
        assert (self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip) == False)
        self.logger.info("Scp connection is working")

        # scale up, do scp and check that the flow has ecmp index now
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        assert pod2.verify_on_setup()
        self.do_scp(client_pod, service.cluster_ip, limit_rate=True)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)
        self.logger.info("test_non_ecmp_to_ecmp passed")
    # end test_non_ecmp_to_ecmp

    @preposttest_wrapper
    def test_ecmp_to_non_ecmp(self):
        ''' Create a service with 2 pods in worker_node_2
            Create a client pod in worker_node_1 which will scp a file.
            Ecmp index should be present in flow.
            Scale down to 1 pod and do scp again, flow should not have ecmp index.
        '''
        compute_label_list, compute_count = \
                self.connections.k8s_client.get_kubernetes_compute_labels()
        compute_selector_1 = {'computenode': compute_label_list[0]}
        if compute_count >= 2:
             compute_selector_2 = {'computenode': compute_label_list[1]}
        else:
             compute_selector_2 = compute_selector_1
        app = 'scp_test'
        labels = {'app': app}
        namespace = self.setup_namespace()

        service = self.setup_ssh_service(namespace=namespace.name,
                                          labels=labels)
        # create client pod
        client_pod = self.setup_ssh_client_pod(namespace=namespace.name,
                compute_node_selector= compute_selector_2)
        assert client_pod.verify_on_setup()

        # create webserver pods
        pod1 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        pod2 = self.setup_ssh_webserver_pod(namespace=namespace.name,
                labels=labels, compute_node_selector=compute_selector_1)
        assert pod1.verify_on_setup()
        assert pod2.verify_on_setup()
        assert service.verify_on_setup()

        # do scp and check that the flow should have ecmp index
        self.do_scp(client_pod, service.cluster_ip, limit_rate=True)
        assert self.validate_ssh(client_pod)
        assert self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip)


        # scale down, do scp and check that scp is broken
        pod2.delete()
        assert self.validate_ssh(client_pod, False)
        assert (self.validate_ecmp_flow(self.inputs.compute_ips,
                                service.cluster_ip, client_pod.pod_ip) == False)
        self.logger.info("test_ecmp_to_non_ecmp passed")
    # end test_ecmp_to_non_ecmp
