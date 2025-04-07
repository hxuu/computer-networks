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
        'networks': ['10.12.0.0']
    },
    {
        'port': 5001,
        'networks': ['10.12.0.0', '10.23.0.0']
    },
    {
        'port': 5002,
        'networks': ['10.23.0.0', '10.34.0.0']
    },
    {
        'port': 5003,
        'networks': ['10.34.0.0', '10.45.0.0']
    },
    {
        'port': 5004,
        'networks': ['10.45.0.0', '10.56.0.0']
    },
    {
        'port': 5005,
        'networks': ['10.56.0.0']
    }
]

configure_rip(routers)

