
"""
collect junos show command in json format, parse the output 
can be applied to any junos commands (bgp sessions state, interface op state, ....) to validate the state of the device
"""

from netmiko import ConnectHandler
import json 

username = 'jcluser'
password = 'Juniper!1'
host = '100.123.1.0'

junos_device = {'device_type': 'juniper_junos', 'host': host, 'username': username, 'password': password}
dev = ConnectHandler(**junos_device)

command = "show chassis hardware"

command_output = dev.send_command(command + "| display json")

# type (command_output)
# command_output is a string 

data_json = json.loads(command_output)
# type (data_json)
# data_json is a dictionnary

device_SN = data_json["chassis-inventory"][0]["chassis"][0]["serial-number"][0]['data']
print ("the SN of device " + host + " is: " + device_SN)

