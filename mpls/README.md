# Multiprotocol Label Switching

## From [wikipedia](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching)

- In an MPLS network, labels are assigned to data packets. Packet-forwarding decisions are made solely on the contents of this label
- MPLS works by prefixing packets with an MPLS header, containing one or more labels. This is called a label stack.

for more details check:

1. [Wikipedia](https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching)
2. [LIVE: Let's learn MPLS with Kelvin Tran!](https://www.youtube.com/watch?v=J7I0DUKCX9c&t=1382s)

## TP MPLS

![topology](screenshots/2025-04-07-08-44-38.png)

### 1. Configurer Routage

Check `./scripts/rip.py` for automatic config. (make sure you have the same topology)

> Results of routing config is in `./results/rip.txt`

### 2. Configurer Les routeurs dans le Domain MPLS sauf les CErouteurs.
### 3. Tester la connectivité.
### 4. Vérifier le trafic dans le Domain MPLS.
### 5. Analyser les Labels via wireshark.
### 6. Analyser LDP via wireshark.

