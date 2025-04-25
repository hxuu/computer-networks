from utils.configure_ip import configure_ip
from utils.rip import configure_rip
from utils.vpn import create_acl, phase1, phase2


def run_configure_ip(port, interface_config):
    """
    interface_config should be a list of dictionaries:
    [{'int': 'f0/0', 'ip': '192.168.1.1', 'mask': '255.255.255.0'}, ...]
    """
    configure_ip(port, interface_config)


def run_rip(router_configs):
    """
    router_configs: list of dicts like:
    [{'port': 5000, 'networks': ['10.1.1.0', '192.168.1.0']}, ...]
    """
    configure_rip(router_configs)


def run_vpn(acl_configs, vpn_peers):
    """
    acl_configs: list of ACL rules (see create_acl)
    vpn_peers: list of VPN peer configs (see phase1/phase2)
    """
    create_acl(acl_configs)
    phase1(vpn_peers)
    phase2(vpn_peers)

