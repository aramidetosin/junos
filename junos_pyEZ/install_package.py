from jnpr.junos import Device
from connect import connect_ssh_key
from rich import print
from lxml import etree
from pprint import pprint
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.sw import SW

PACKAGE = '/var/tmp/junos-openconfig-0.0.0.10-1-signed.tgz'

def progress_callback(dev, report):
    print(report)

if __name__ == "__main__":
    with connect_ssh_key(host='192.168.1.226') as dev:
        sw = SW(dev)
        ok = sw.install(package=PACKAGE, no_copy=True, validate=False, progress=progress_callback)