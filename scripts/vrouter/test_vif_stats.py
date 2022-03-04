'''
This FT automation implementation will perform vif0 statistics check

Tested on dpdk compute Bond configuration
'''
from builtins import str
from common.vrouter.base import BaseVrouterTest
from tcutils.wrappers import preposttest_wrapper
import test
import string
class TestvifStats(BaseVrouterTest):

    @classmethod
    def setUpClass(cls):
        super(TestvifStats, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestvifStats, cls).tearDownClass()
    def get_vif_stats(self,compute_ip):
        self.logger.info(compute_ip)
        ''' check the vif stats on all the vif interface'''
        for vif_id in range(0,5):
            #implementwith separate RX/TX packet commands to avoid another loop
            vif_rx_cmd = "vif --get " + str(vif_id) + " | grep " + '"RX packets" ' + "| tr  -s ' ' | cut -f1-3 -d ' '"
            self.logger.info(vif_rx_cmd)
            vif_out = self.inputs.run_cmd_on_server(compute_ip,vif_rx_cmd)
            assert vif_out, "vif stats for %s is not working" % vif_rx_cmd
            if not "RX packets" in vif_out:
                assert False, "RX packets is not available"
            else:
                result = vif_out.split()
                rx_pkt_cnt = result[1].split(":")
                get_vif_rx_pkt_cnt = int(rx_pkt_cnt[1])
                self.logger.info(get_vif_rx_pkt_cnt)
            
            vif_tx_cmd = "vif --get " + str(vif_id) + " | grep " + '"TX packets" ' + "| tr  -s ' ' | cut -f1-3 -d ' '"
            vif_out = self.inputs.run_cmd_on_server(compute_ip,vif_tx_cmd)
            self.logger.info(vif_out)
            assert vif_out, "vif stats for %s is not working" % vif_tx_cmd
            if not "TX packets" in vif_out:
                assert False, "TX packets is not available"
            else:
                result = vif_out.split()
                tx_pkt_cnt = result[1].split(":")
                get_vif_tx_pkt_cnt = int(tx_pkt_cnt[1])
                self.logger.info(get_vif_tx_pkt_cnt)
        return True
     #end get_vif_stats

    def clear_vif_stats(self,compute_ip):
        self.logger.info(compute_ip)
        vif_clr_cmd = "vif --clear 0"
        vif_clr_out = self.inputs.run_cmd_on_server(compute_ip, vif_clr_cmd)
        self.logger.info(vif_clr_out)
        output = "Vif stats cleared successfully"
        if not output in vif_clr_out:
            assert False, "Error while clearing vif stats"
        return True
    # end clear_vif_stats

    @test.attr(type=['sanity', 'vcenter_compute', 'dev_reg'])
    @preposttest_wrapper
    def test_vif_statistics(self):
        """ 
        Description: 
            Verify vif statistics
            Vm's across compute node
        steps:
            1. create 1 VN and launch 2 VMs in compute node 
            2. client and server VMs on same node
            3. send icmp traffic assert if ping is not working
            4. get_vif_stats to check vif interface 
            5. clear_vif_stats to clear vif interface stats
            6. Repeat step4
        Pass criteria:
            1. If output of vif stats/clear execute successfully from compute 
        """
        vn_fixtures = self.create_vns(count=1)
        self.verify_vns(vn_fixtures)
        vn1_fixture = vn_fixtures[0]
        compute_hosts = self.orch.get_hosts()
        client_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0])
        server_fixtures = self.create_vms(vn_fixture= vn1_fixture,count=1,
            node_name=compute_hosts[0])
        self.verify_vms(client_fixtures)
        self.verify_vms(server_fixtures)
        assert client_fixtures[0].ping_with_certainty(server_fixtures[0].vm_ip, expectation=True), "ping failed"
        compute_ip = server_fixtures[0].vm_node_ip
        stats_pre_clr = self.get_vif_stats(compute_ip)
        self.clear_vif_stats(compute_ip)
        stats_post_clr = self.get_vif_stats(compute_ip)
        assert stats_pre_clr <= stats_post_clr, "vif_stats failed"
