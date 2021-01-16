from jnpr.junos import Device
from connect import connect_ssh_key
from rich import print
from lxml import etree
from pprint import pprint
from jnpr.junos.utils.config import Config

if __name__ == "__main__":
    data = 'set system services netconf traceoptions file test.log'
    with connect_ssh_key(host='192.168.1.231') as devices:
        with Config(devices, mode='exclusive') as conf:
            conf.load(data, format='set')
            conf.diff()
            diff = conf.diff()
            if diff is None:
                print("Config already up to date")
            else:
                print(diff)
                conf.commit()