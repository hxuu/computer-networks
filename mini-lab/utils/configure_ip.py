#!/usr/bin/env python3

from netmiko import ConnectHandler

cisco_2691 = {
    'device_type': 'cisco_ios_telnet',
    'host': '127.0.0.1',
    'port': 5000
}


def configure_ip(port, interfaces):
    cisco_2691 = {
        'device_type': 'cisco_ios_telnet',
        'host': '127.0.0.1',
        'port': port
    }

    net_connect = ConnectHandler(**cisco_2691)

    # net_connect.send_command('enable')
    # net_connect.send_command('configure terminal')

    for i in range(len(interfaces)):
        config_commands = [
            f'int {interfaces[i]["int"]}',
            f'ip address {interfaces[i]["ip"]} {interfaces[i]["mask"]}',
            'no shutdown'
        ]
        output = net_connect.send_config_set(config_commands)

    output = net_connect.send_command('show ip int brief')
    print(output)
    print('================================================================================')
    net_connect.disconnect()
    # net_connect.send_command('copy running-config startup-config')
    # net_connect.send_command('write memory')


# # testing
# r1 = [
#     {
#         'int': 's1/0',
#         'ip': '10.1.1.2',
#         'mask': '255.255.255.252'
#     },
#     {
#         'int': 'f0/0',
#         'ip': '192.168.1.1',
#         'mask': '255.255.255.0'
#     },
# ]
# configure_ip(5000, r1)

# # testing
# r2 = [
#     {
#         'int': 's1/0',
#         'ip': '10.1.1.1',
#         'mask': '255.255.255.252'
#     },
#     {
#         'int': 'f0/0',
#         'ip': '192.168.2.1',
#         'mask': '255.255.255.0'
#     },
#     {
#         'int': 's1/1',
#         'ip': '10.2.2.1',
#         'mask': '255.255.255.252'
#     }
# ]
# configure_ip(5001, r2)

# # testing
# r3 = [
#     {
#         'int': 's1/0',
#         'ip': '10.2.2.2',
#         'mask': '255.255.255.252'
#     },
#     {
#         'int': 'f0/0',
#         'ip': '192.168.3.1',
#         'mask': '255.255.255.0'
#     },
# ]
# configure_ip(5002, r3)
