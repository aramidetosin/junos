#! /usr/bin/python3

# Perform required imports
import json
from pprint import pprint
from rich import print

# If this module is run as a standalone script
if __name__ == "__main__":

    print("Reading the file...")

    # Work with file using context manager syntax, which
    # opens and closes the file automatically
    with open("show_route_output.json") as f:
        # Load JSON data from file
        route_data = json.load(f)

    for i in route_data['route-information'][0]['route-table']:
        print(i['table-name'][0]['data'])
        for j in i['rt']:
            print(f"{j['rt-destination'][0]['data']}: {j['rt-entry'][0]['protocol-name'][0]['data']}")

    # Pretty-print data loaded from JSON
    # print(route_data['route-information'][0]['route-table'][0]['table-name'][0]['data'])

    # for i in route_data['route-information'][0]['route-table']['rt']:
    #     print(i)
        # print(f"{i['rt-destination'][0]['data']}: {i['rt-entry'][0]['protocol-name'][0]['data']} ")