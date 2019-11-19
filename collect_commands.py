"""
this script collects the output of show commands in various formats (text, xml and json) and save it in the current directory
"""

from netmiko import ConnectHandler

username = 'jcluser'
password = 'Juniper!1'
host = '100.123.1.0'
junos_device = {'device_type': 'juniper_junos', 'host': host, 'username': username, 'password': password}
dev = ConnectHandler(**junos_device)

commands = ["show chassis hardware", "show system information"]
for command in commands: 
  # collect a command with an text format
  command_output = dev.send_command(command)
  f=open(command + ".txt", "w")
  f.write(command_output)
  f.closed
  # collect the command with an xml representation 
  command_output = dev.send_command(command + " | display xml")
  f=open(command + ".xml", "w")
  f.write(command_output)
  f.closed
  # collect the command in json format
  command_output = dev.send_command(command + "| display json")
  f=open(command + ".json", "w")
  f.write(command_output)
  f.closed

dev.disconnect()

