#!/usr/bin/env python3

from netmiko import ConnectHandler


def configure_rip(routers):

    for i in range(len(routers)):

        cisco_2691 = {
            'device_type': 'cisco_ios_telnet',
            'host': '127.0.0.1',
            'port': routers[i]['port']
        }
        net_connect = ConnectHandler(**cisco_2691)

        config_commands = [
            'router rip',
            'version 2',
            'no auto-summary',
            *[f'network {network}' for network in routers[i]["networks"]]
        ]
        net_connect.send_config_set(config_commands)

        output = net_connect.send_command('show ip route')
        print('================================================================================')
        print(output)
        print('================================================================================')

        net_connect.disconnect()


# testing
routers = [
    {
        'port': 5000,
        'networks': ['10.1.1.0', '192.168.1.0']
    },
    {
        'port': 5001,
        'networks': ['10.2.2.0', '192.168.2.0']
    },
    {
        'port': 5002,
        'networks': ['10.2.2.0', '192.168.3.0']
    }
]
configure_rip(routers)
