from jinja2 import Template
from yaml import load, FullLoader
from netmiko import ConnectHandler
import json
import time
from pprint import pprint as pp

# template to configure junos
f=open('junos.j2')
junos_template = Template(f.read())
f.close()

# get variables
f=open('vars.yml', 'r')
vars = load(f.read(), Loader=FullLoader)
f.close()

print("generating and loading configuration")
for item in vars:
   host_vars = vars[item]
   device = host_vars['netmiko']
   dev = ConnectHandler(**device)
   f=open(host_vars['netmiko']['host'] + '.txt','w')
   f.write(junos_template.render(host_vars))
   f.close()
   load = dev.send_config_from_file(config_file=host_vars['netmiko']['host'] + '.txt')
   commit = dev.commit(confirm=False, check=False, comment='commited from netmiko')
   dev.disconnect()

print ("waiting 15 seconds before validating BGP sessions state")
time.sleep(15)
for item in vars:
   host_vars = vars[item]
   device = host_vars['netmiko']
   dev = ConnectHandler(**device)
   command = "show bgp neighbor"
   command_output = dev.send_command(command + "| display json")
   data_json = json.loads(command_output)
   print ("Device " + host_vars['netmiko']['host'])
   for neighbor in data_json["bgp-information"][0]["bgp-peer"]: 
     print ("session with " + neighbor["peer-address"][0]['data'] + " is "+ neighbor["peer-state"][0]['data'])  
   dev.disconnect()


