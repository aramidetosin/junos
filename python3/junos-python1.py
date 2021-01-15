#! /usr/bin/python3
from rich import print
import re

my_interfaces = ["xe-0/0/0", "ge-0/0/0", "et-0/0/0"]

for interface in my_interfaces:
    if interface.startswith("ge-"):
        print(f"{interface} is a 1G interface")
    elif interface.startswith("xe-"):
        print(f"{interface} is a 10G interface")
    elif interface.startswith("et-"):
        print(f"{interface} is a 100G interface")
    else:
        print("Couldn't recognize the speed of interface: {interface}")

print("Interface Testing Finished")



for interface in my_interfaces:
    if re.match("ge-.*", interface):
        print(f"{interface} is a 1G interface")


new_interfaces = [f'ge-0/0/{i}' for i in range(16)]
new_interfaces.append("fxp0")
print(new_interfaces)

print(new_interfaces.pop())

new_interfaces.insert(0, "fxp0")
print(new_interfaces)

sliced_list = []
for i in range(0, len(new_interfaces)):
    if re.match("ge-0/0/0.*", new_interfaces[i]):
        sliced_list = new_interfaces[i:i+6]

print(sliced_list)


my_dict = {
    "user": "root",
    "device": ("Juniper", "Junos"),
    "interfaces": new_interfaces
}

print(my_dict)
new_interfaces.append("lo0")
print(my_dict)

my_interfaces = ['fe-0/0/0', 'fe-0/0/1']
print(my_interfaces)
print(my_dict)

my_set = set(my_dict['interfaces'])
print(my_set)