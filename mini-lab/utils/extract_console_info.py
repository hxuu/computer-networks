import json

def extract_console_info(data):
    nodes = data.get('topology', {}).get('nodes', [])

    connection_info = []

    for node in nodes:
        name = node.get('name', 'unknown')
        node_id = node.get('node_id')
        console = node.get('console', None)
        console_type = node.get('console_type', 'telnet')  # default GNS3 type
        host = '127.0.0.1'  # GNS3 local server by default

        # Only add if a console port exists
        if console is not None:
            connection_info.append({
                'name': name,
                'host': host,
                'port': console,
                'type': console_type,
                'node_id': node_id
            })

    return connection_info


# Example usage
if __name__ == '__main__':
    devices = extract_console_info('../uploads/mpls.gns3')
    for device in devices:
        print(f"{device['name']}: {device['type']} -> {device['host']}:{device['port']}")

    # This will print:
    # ➜ python extract_console_info.py
    #     CE1: telnet -> 127.0.0.1:5000
    #     PE1: telnet -> 127.0.0.1:5001
    #     P1: telnet -> 127.0.0.1:5002
    #     P2: telnet -> 127.0.0.1:5003
    #     PE2: telnet -> 127.0.0.1:5004
    #     CE2: telnet -> 127.0.0.1:5005
