from jnpr.junos import Device
from connect import connect_ssh_key
from rich import print
from lxml import etree
from pprint import pprint
from jnpr.junos.utils.config import Config

if __name__ == "__main__":
    with connect_ssh_key(host='192.168.1.231') as devices:
        config = Config(devices)

        data = """ interfaces {
        ge-0/0/3 {
            description "Connection to vMX2";
            unit 0 {
                family inet {
                    address 192.168.100.1/24;
                }
            }
        }
    }"""
        config.lock()
        config.load(data, format='text')
        config.pdiff
        if config.commit_check():
            config.commit()
        else:
            config.rollback()
        config.unlock()
