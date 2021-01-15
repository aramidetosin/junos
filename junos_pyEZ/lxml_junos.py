from jnpr.junos import Device
from connect import connect_ssh_key
from rich import print
from lxml import etree
from pprint import pprint

if __name__ == "__main__":
    with connect_ssh_key(host='192.168.1.211') as devices:
        print(devices.display_xml_rpc('show route', format="text"))
        print(devices.display_xml_rpc('show interfaces terse', format="text"))


        # print(devices.rpc.get_route_information({'format':'text'}))

        route_lxml_element = devices.rpc.get_route_information(table='inet.0')
        # print(etree.tostring(route_lxml_element))
        list_of_routes = route_lxml_element.findall('.//rt')
        for route in list_of_routes:
            print(f"{route.findtext('rt-destination').strip()}: {route.findtext('rt-entry/protocol-name').strip()}")

        interface_lxml_element = devices.rpc.get_interface_information(interface_name='lo0.0')
        # print(interface_lxml_element)
        list_of_interfaces = interface_lxml_element.findall(".//logical-interface")
        # print(list_of_interfaces)

        for locgical_intf in list_of_interfaces:
            print(f"{locgical_intf.findtext('name').strip()}: {locgical_intf.findtext('address-family/interface-address/ifa-local').strip()}")

        interface_lxml_element = devices.rpc.get_interface_information(interface_name='lo0', extensive=True)
        list_of_interfaces = interface_lxml_element.findall(".//link-level-type")

        # print(list_of_interfaces)
        for link_level in list_of_interfaces:
            print(f"{link_level.text}")

        cnf = devices.rpc.get_config()
        print(etree.tostring(cnf))

        cnf = devices.rpc.get_config(filter_xml=etree.XML('<configuration><interfaces/></configuration>'))
        print(etree.tostring(cnf))

        sw = devices.rpc.get_software_information()
        print(etree.tostring(sw, encoding='unicode'))

        # sw_info_text = devices.rpc.get_software_information({'format':'text'})
        sw_info_text = devices.rpc.get_software_information({'format':'json'})
        # print(etree.tostring(sw_info_text))
        pprint(sw_info_text)