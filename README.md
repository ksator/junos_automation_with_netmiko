[![Build Status](https://travis-ci.org/ksator/junos_automation_with_netmiko.svg?branch=master)](https://travis-ci.org/ksator/junos_automation_with_netmiko)  

Netmiko is a multi-vendor python library to simplify SSH connections to network devices   
This repo has Netmiko examples for Junos.  
It convers how to: 
- connect to devices using Netmiko
- generate devices configuration files from templates and vars
- Load configuration files on devices using Netmiko
- Commit configuration changes using Netmiko
- collect `show commands` in various format (JSON, XML, text) using Netmiko
- Parse the data collected in JSON format (to validate BGP sessions state as example. All Junos show commands can be collected in JSON format so this approach can be applied to all Junos show commands)  
- Use Netmiko and NTC TextFSM templates to validate some op states (when an NTC TextFSM template is available)  

Visit the repository [wiki](https://github.com/ksator/junos_automation_with_netmiko/wiki) to get the instructions  


