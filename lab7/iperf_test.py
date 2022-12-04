from conftest import client
from iperf_parser import iperf_parser

class TestSuite():
    def test_iperf3_client_connection(self, client):
        assert client[0] is not None
    
    def test_iperf3_client_response(self, client):
        for value in iperf_parser(client[0]):
            assert value['transfer'] > 2.2
            assert value['bitrate'] > 2.0

