from jnpr.junos import Device
from rich import print

def connect_ssh(host, user='root', passwd='juniper1'):
    dev = Device(host, user='root', passwd='juniper1')
    # return dev.open()
    return dev

key='/home/vagrant/junos/juniper-hosts.key'

def connect_ssh_key(host, ssh_private_key_file=key):
    dev = Device(host, ssh_private_key_file=key)
    return dev

if __name__ == "__main__":
    # device = connect_ssh(host="192.168.1.211", user='root', passwd='juniper1')
    # print(device.facts)
    with connect_ssh(host="192.168.1.211") as device:
        print(device.facts)

    with connect_ssh_key(host='192.168.1.211') as devices:
        print(devices.facts)

    # dev = Device(host='192.168.1.211', ssh_private_key_file='/home/vagrant/junos/juniper-hosts.key')
    # dev.open()
    # print(dev.facts)
    # dev.close()
