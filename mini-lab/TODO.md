# ✅ TODO - GNS3-Based Automated Network Configuration Interface

This file outlines the key tasks required to complete the mini-lab project for *Réseaux 2* using `.gns3` files for topology-aware network automation.

---

## 📁 Project Structure Setup

- [x] Initialize Flask project structure
- [x] Create folders: `templates/`, `static/`, `uploads/`, `assets/`, `app/`
- [x] Create main files: `main.py`, `routes.py`, `gns3_parser.py`, `automation.py`
- [x] Add and test `requirements.txt`

---

## 🔄 GNS3 File Handling

- [ ] Implement file upload route
- [ ] Validate `.gns3` file type
- [ ] Store uploaded file in `/uploads`
- [ ] Parse `.gns3` JSON to extract:
  - [ ] Nodes (names, types, positions, images)
  - [ ] Links (connections between nodes)
  - [ ] SVG GUI elements
  - [ ] SSH/console connection info (host, port, credentials)

---

## 🧠 Topology Rendering

- [ ] Generate browser-friendly SVG topology
- [ ] Position nodes based on GUI coordinates
- [ ] Make nodes clickable to open configuration panels
- [ ] Show node type and possible actions on click

---

## ⚙️ Automation Interface

- [ ] Create HTML/JS frontend to display config options per device
- [ ] Display only context-relevant actions (e.g., VLANs only for switches)
- [ ] Add form for custom commands if needed

---

## 🚀 Backend Automation

- [ ] Build `automation.py` with:
  - [ ] Netmiko SSH login (from parsed `.gn

