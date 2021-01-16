# http://192.168.1.226:8080/rpc/get-interface-information
# curl -u "admin:juniper1"  "http://192.168.1.226:8080/rpc/get-interface-information@format=text?interface-name=ge-0/0/1&terse="

# curl -u "admin:juniper1"  "http://192.168.1.226:8080/rpc/" -d "<get-interface-information><terse/></get-interface-information><get-bgp-summary-information/>"

# curl http://192.168.1.226:8080/rpc/get-bgp-summary-information -u "admin:juniper1" -H "Content-Type: application/xml" -H "Accept: text/plain"

# http://192.168.1.226:8080/rpc/get-route-information@format=json

# http://192.168.1.226:8080/rpc/get-route-information@format=json?active-path=

# http://192.168.1.226:8080/rpc/get-route-information@format=text?active-path=

# http://192.168.1.226:8080/rpc/get-route-information@format=text?active-path=&table=inet.0

# http://192.168.1.226:8080/rpc/get-interface-information@format=text?interface-name=ge-0/0/1&terse=

# curl 'http://192.168.1.226:8080/rpc/get-interface-information@format=text?interface-name=ge-0/0/1&terse' -u "admin:juniper1"

# <get-config>
# <source>
# <running/>
# </source>
# <filter type="subtree">
# <configuration>
# <system>
# <services/>
# </system>
# </configuration>
# </filter>
# </get-config>

import requests
from lxml import etree
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


USER = "admin"
PASSWORD = "juniper1"
DEVICES = ["192.168.1.231"]

CONFIG_FILTER = """
<get-config>
<source>
<running/>
</source>
<filter type="subtree">
<configuration>
<system>
<services/>
</system>
</configuration>
</filter>
</get-config>
"""

# url = f"http://{DEVICES}:8080/rpc"

if __name__ == '__main__':
    for device in DEVICES:
        # print(f"http://{device}:8080/rpc")
        response = requests.post(f"https://{device}:8080/rpc", data=CONFIG_FILTER, 
        auth=(USER, PASSWORD),
        verify=False, 
        headers={"Accept": "application/xml", "Content-Type": "application/xml"}
        )

        XML_LINES = "\n".join(response.text.splitlines()[3:-1])
        # print(response.text)
        # print(XML_LINES)
        respnse_XML = etree.fromstring(XML_LINES)
        telnet_enabled = len(respnse_XML.xpath("configuration/system/services/telnet")) != 0
        ftp_enabled = len(respnse_XML.xpath("configuration/system/services/ftp")) != 0

        if telnet_enabled or ftp_enabled:
            print(f"Warning: Device {device} has disallowed service enabled")
        else:
            print(f"Device {device} is ok")