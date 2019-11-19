from netmiko import ConnectHandler
import json

username = 'jcluser'
password = 'Juniper!1'
vMX1 = {'device_type': 'juniper_junos', 'host': '100.123.1.0', 'username': username, 'password': password}
vMX2 = {'device_type': 'juniper_junos', 'host': '100.123.1.1', 'username': username, 'password': password}
all_vMX = [ vMX1, vMX2]

for vmx in all_vMX:
   dev = ConnectHandler(**vmx)
   command = "show bgp neighbor"
   command_output = dev.send_command(command + "| display json")
   data_json = json.loads(command_output)
   print ("Device " + vmx["host"])
   for neighbor in data_json["bgp-information"][0]["bgp-peer"]: 
     print ("session with " + neighbor["peer-address"][0]['data'] + " is "+ neighbor["peer-state"][0]['data'])  
   dev.disconnect()

