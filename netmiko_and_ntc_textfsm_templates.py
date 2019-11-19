
"""
Netmiko and NTC TextFSM templates 
Refer to the wiki https://github.com/ksator/junos_automation_with_netmiko/wiki/Netmiko-and-NTC-TextFSM-templates for the requirements
"""

from netmiko import ConnectHandler
from pprint import pprint as pp

username = 'jcluser'
password = 'Juniper!1'
host = '100.123.1.0'

junos_device = {'device_type': 'juniper_junos', 'host': host, 'username': username, 'password': password}
dev = ConnectHandler(**junos_device)

# use NTC TextFSM template and Netmiko 
# `sh inte` is a possible abbreviation of `show interfaces`
interfaces_with_data_structured = dev.send_command("sh inte", use_textfsm=True)

# interfaces_with_data_structured is a list of dictionaries
# type(interfaces_with_data_structured)

# for item in interfaces_with_data_structured:
#   print (item['interface'])

for item in interfaces_with_data_structured:
  if (item['admin_state'] == 'Enabled') and (item["link_status"] != "Up"): 
    print ("warning: interface " + item['interface'] + " admin state is " + item['admin_state'] + " but op state is " + item["link_status"])  


