# 🌐 GNS3-Based Automated Network Configuration Interface

This project is a visual and automated network configuration tool built using **Flask**, **vanilla HTML/CSS/JS**, and designed to work with **GNS3 topologies**.

## 🎯 Objective

To automate network configuration through an intuitive web interface by uploading a GNS3 project file (`.gns3`) and visually interacting with the topology.

## 📁 How It Works

1. **Upload a GNS3 Project (.gns3 file)**
   The `.gns3` file is a JSON document describing the network topology, nodes, links, and their SVG/GUI positions.

2. **Render the Topology**
   The web interface parses the topology and draws it using SVGs in the browser, preserving the positions and device images.

3. **Enable Targeted Automation**
   Based on the parsed topology and node types, the interface offers automation options tailored to each device (e.g., VLANs for switches, OSPF for routers).

## 🧠 Features

- Upload and parse `.gns3` files
- Display topology visually in-browser
- Clickable devices for interaction
- Contextual automation options per node type
- Backend automation using SSH (Netmiko)

## 💻 Tech Stack

- **Frontend**: Vanilla HTML, CSS, JS
- **Backend**: Python (Flask)
- **Network Automation**: Netmiko
- **Topology Source**: GNS3 Project Files (.gns3)

---

### Developer specific

check `./TODO.md` to see what's next to be implemented.

### References

- https://gns3-server.readthedocs.io/en/stable/file_format.html
- https://github.com/cidrblock/drawthe.net
- https://davidban77.hashnode.dev/making-your-network-topology-come-to-virtual-life-with-drawthenet-and-gns3fy-ck9kjsujb004jzss19c5stx6t

### Schema reference

the .gns3 file is a json file that contains nodes and links:

1. nodes is a list that contains a list of nodes. Each node contains the following info:
- `node_id`
- name
- console (port number)
- `port_name_format`  ('Ethernet{0}')
- properties (which has key image to decide if it's a router or switch)
    - for example: `'image': 'c2691-adventerprisek9-mz.124-25d.image',`

```
[{'aux': None,
  'aux_type': 'none',
  'compute_id': 'local',
  'console': 5000,
  'console_auto_start': False,
  'console_type': 'telnet',
  'custom_adapters': [],
  'first_port_name': None,
  'height': 60,
  'label': {'rotation': 0,
            'style': 'font-family: TypeWriter;font-size: 10.0;font-weight: '
                     'bold;fill: #000000;fill-opacity: 1.0;',
            'text': 'CE1',
            'x': 14,
            'y': -25},
  'locked': False,
  'name': 'CE1',
  'node_id': 'db7d1d0c-8d39-4b52-b1c6-8f0528078963',
  'node_type': 'dynamips',
  'port_name_format': 'Ethernet{0}',
  'port_segment_size': 0,
  'properties': {'auto_delete_disks': True,
                 'builtin': False,
                 'chassis': None,
                 'clock_divisor': 8,
                 'created_at': '2025-04-07T08:01:46',
                 'disk0': 0,
                 'disk1': 0,
                 'dynamips_id': 1,
                 'exec_area': 64,
```

2. links is a list that contains a list of links between nodes (which is also a list). Each link contains the following info:
- nodes (a list containing info about the linked nodes)
    - `node_id`
    - label (which is an object that contains 'text' to mark the interface linked)

example result:
```
[{'filters': {},
  'link_id': '00f55b33-08a2-41ad-8b50-467379fb6240',
  'link_style': {'color': None, 'type': None, 'width': None},
  'nodes': [{'adapter_number': 0,
             'label': {'rotation': 0,
                       'style': 'font-family: TypeWriter;font-size: '
                                '10.0;font-weight: bold;fill: '
                                '#000000;fill-opacity: 1.0;',
                       'text': 'f0/0',
                       'x': 69,
                       'y': 30},
             'node_id': 'db7d1d0c-8d39-4b52-b1c6-8f0528078963',
             'port_number': 0},
            {'adapter_number': 0,
             'label': {'rotation': 0,
                       'style': 'font-family: TypeWriter;font-size: '
                                '10.0;font-weight: bold;fill: '
                                '#000000;fill-opacity: 1.0;',
                       'text': 'f0/1',
                       'x': -32,
                       'y': 30},
             'node_id': '2184ea02-f5c3-43e3-9a5f-d5740db8a273',
             'port_number': 1}],
  'suspend': False},
```


