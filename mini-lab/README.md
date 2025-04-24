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
