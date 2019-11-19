
from jinja2 import Template
from yaml import load, FullLoader
from netmiko import ConnectHandler

# template to configure junos
f=open('junos.j2')
junos_template = Template(f.read())
f.close()

# get variables
f=open('vars.yml', 'r')
vars = load(f.read(), Loader=FullLoader)
f.close()

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

