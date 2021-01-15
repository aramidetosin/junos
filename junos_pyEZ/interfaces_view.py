from jnpr.junos import Device
from connect import connect_ssh_key
from rich import print
from pprint import pprint
from lxml import etree

if __name__ == "__main__":
    with connect_ssh_key(host='192.168.1.212') as dev:
        print(dev.facts)

        config_json = dev.rpc.get_config(filter_xml='interfaces')
        list_of_interfaces = config_json.findall(".//interface")
        # print(list_of_interfaces)
        for i in list_of_interfaces:
            print(f"{i.findtext('name')} ------> {i.findtext('unit/family/inet/address/name')}")


        print('\nInterface operational status')
        rpc_result = dev.rpc.get_interface_information()
        # etree.dump(rpc_result)

        interfaces = rpc_result.xpath("physical-interface")
        for i in interfaces:
            name = i.findtext('name').strip()
            status = i.findtext('oper-status').strip()
            if name.startswith("ge-") or name.startswith("lo0"):
                print(f"Interface: {name}, Status: {status}")