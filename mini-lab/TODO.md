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

- [x] Implement file upload route
- [x] Validate `.gns3` file type
- [x] Store uploaded file in `/uploads`
- [x] View `.gns3` as topology:
    - [x] Parse the .gns3 as a json file and extract useful info
    - [x] Create the YAML file to be used with drawthe.net
    - [x] Convert the YAML file into a picture
    - [x] Render that picture to the user
- [ ] Parse `.gns3` JSON to extract SSH/console connection info (host, port, credentials)

---

## ⚙️ Automation Interface

- [ ] Create HTML/JS frontend to display config options per device
- [ ] Display only context-relevant actions (e.g., VLANs only for switches)
- [ ] Add form for custom commands if needed

---

## 🚀 Backend Automation

- [ ] Build `automation.py` with:
  - [ ] Netmiko SSH login (from parsed `.gns3`)

