#!/usr/bin/env python3

import inspect
from netmiko import ConnectHandler

cisco_2691 = {
    'device_type': 'cisco_ios_telnet',
    'host': '127.0.0.1',
    'port': 5000
}


def create_acl(routers):
    for router in routers:
        cisco_2691 = {
                'device_type': 'cisco_ios_telnet',
                'host': '127.0.0.1',
                'port': router['port']
        }

        net_connect = ConnectHandler(**cisco_2691)
        config_commands = [
            f"access-list 100 permit ip {router['from']['network']} {router['from']['inv_mask']} {router['to']['network']} {router['to']['inv_mask']}"
        ]
        output = net_connect.send_config_set(config_commands)

        output = net_connect.send_command('show access-lists') # for verification
        print(f"-- Verfication step for {inspect.currentframe().f_code.co_name} ({router['name']}) --")
        print(output)
        print('================================================================================')
        net_connect.disconnect()
        # output = net_connect.send_command('copy running-config startup-config')
        # output = net_connect.send_command('write memory')


def phase1(peers):
    for peer in peers:
        cisco_2691 = {
                'device_type': 'cisco_ios_telnet',
                'host': '127.0.0.1',
                'port': peer['port']
        }

        net_connect = ConnectHandler(**cisco_2691)

        config_commands = [
            "crypto isakmp policy 10",
            "encryption aes 256",
            "authentication pre-share",
            "group 2",   # Groups define the level of security of the key exchange -> 2 is moderate
            "exit",
            f"crypto isakmp key cisco address {peer['remote']}"
        ]
        net_connect.send_config_set(config_commands)

        # output = net_connect.send_command('show crypto isakmp sa') # for verification
        print(f"-- Verfication step for {inspect.currentframe().f_code.co_name} ({peer['name']}) --")
        # print(output)
        print("Nothing to show here...")
        print('================================================================================')
        net_connect.disconnect()
        # output = net_connect.send_command('copy running-config startup-config')
        # output = net_connect.send_command('write memory')


def phase2(peers):
    for peer in peers:
        cisco_2691 = {
                'device_type': 'cisco_ios_telnet',
                'host': '127.0.0.1',
                'port': peer['port']
        }

        net_connect = ConnectHandler(**cisco_2691)

        config_commands = [
            # phase 2 related
            "crypto ipsec transform-set VPN-SET esp-3des esp-sha-hmac",

            # tie it all together (phase1/2)",
            "crypto map VPN-MAP 10 ipsec-isakmp",
            f"set peer {peer['remote']}",
            "description SOME USEFUL DESCRIPTION",
            "set pfs group2",
            "set security-association lifetime seconds 86400",
            "set transform-set VPN-SET",
            "match address 100",

            # Activate VPN on a given interface",
            f"interface {peer['interface']}",
            "crypto map VPN-MAP",
        ]
        net_connect.send_config_set(config_commands)

        output = net_connect.send_command('show crypto ipsec sa') # for verification
        print(f"-- Verfication step for {inspect.currentframe().f_code.co_name} ({peer['name']}) --")
        print(output)
        print('================================================================================')
        net_connect.disconnect()
        # output = net_connect.send_command('copy running-config startup-config')
        # output = net_connect.send_command('write memory')


# # testing
# routers = [
#     {
#         'name': 'r1',
#         'port': 5000,
#         'from': {
#             'network': '192.168.1.0',
#             'inv_mask': '0.0.0.255'
#         },
#         'to': {
#             'network': '192.168.3.0',
#             'inv_mask': '0.0.0.255',
#         }
#     },
#     {
#         'name': 'r3',
#         'port': 5002,
#         'from': {
#             'network': '192.168.3.0',
#             'inv_mask': '0.0.0.255'
#         },
#         'to': {
#             'network': '192.168.1.0',
#             'inv_mask': '0.0.0.255'
#         }
#     },
# ]
# create_acl(routers)


# peers = [
#     {
#         'name': 'r1',
#         'port': 5000,
#         'remote': '10.2.2.2',
#         'interface': 's1/0'
#     },
#     {
#         'name': 'r3',
#         'port': 5002,
#         'remote': '10.1.1.2',
#         'interface': 's1/0'
#     }
# ]
# phase1(peers)
# phase2(peers)
