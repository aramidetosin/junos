from jnpr.junos import Device
from connect import connect_ssh_key
from rich import print
from pprint import pprint
from lxml import etree
from jnpr.junos.utils.config import Config
from time import sleep

if __name__ == "__main__":
    interface = 'ge-0/0/3'
    data = f"set interfaces {interface} disable"
    delete_data = f"delete interfaces {interface} disable"
    with connect_ssh_key(host='192.168.1.212') as dev:
        with Config(dev, mode='exclusive') as conf:
            print(f"Disabling the interface {interface}...")
            conf.load(data, format='set')
            # diff = conf.diff()
            # print(diff)
            conf.pdiff()
            conf.commit()
            print(f"Commit completed, waiting")
            sleep(5)

            print(f"Enabling interface {interface} .....")
            conf.load(delete_data, format='set')
            # diff = conf.diff()
            # print(diff)
            conf.pdiff()
            conf.commit()
            print('Finished')