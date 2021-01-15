from jnpr.junos import Device
from connect import connect_ssh_key
from rich import print
from pprint import pprint

if __name__ == "__main__":
    neighors = {}
    peer_established = 0
    peers_other = 0
    with connect_ssh_key(host='192.168.1.212') as dev:
        bgp_data = dev.rpc.get_bgp_summary_information()
        bgp_data_count = bgp_data.xpath("bgp-peer/peer-state")
        # bgp_data_count = bgp_data.findall(".//bgp-peer")
        dd = bgp_data.xpath("bgp-peer/peer-address")

        for i in range(0, len(bgp_data_count)):
            if bgp_data_count[i].text == 'Established':
                neighors[dd[i].text] = bgp_data_count[i].text
            # if i.findtext('peer-state') == "Established":
                peer_established += 1
            else:
                neighors[dd[i].text] = bgp_data_count[i].text
                peers_other +=1

    print(f"Sessions in Established state is {peer_established} out of {peer_established+peers_other}")
    pprint(neighors)
    if peers_other != 0:
        print(f"Waring! there are some sessions in a non-established state")
        exit(1)