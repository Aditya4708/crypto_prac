# Nmap Scanner Menu — `nmap.py`

## 📖 Topic Brief
**Nmap (Network Mapper)** is a free, open-source tool for network discovery and security auditing. This script provides a menu-based interface that generates the correct Nmap command for various scan types.

**Category:** Network Security / Reconnaissance Tool

---

## 🔍 Line-by-Line Explanation

| Line | Code | Logic |
|------|------|-------|
| 1-7 | `print("1. Ping Scan")` ... | Displays 7 scan type options |
| 9 | `choice = int(input(...))` | User selects scan type |
| 10 | `target = input(...)` | User enters target IP |
| 12-13 | `-sn` | **Ping Scan** — discovers live hosts, no port scan |
| 15-16 | `-sT` | **TCP Connect Scan** — full 3-way handshake, reliable but detectable |
| 18-19 | `-sU` | **UDP Scan** — for DNS(53), DHCP(67), SNMP(161) services |
| 21-22 | `-O` | **OS Detection** — fingerprints the target OS |
| 24-25 | `-sX` | **Xmas Scan** — stealth scan using FIN+PSH+URG flags |
| 27-28 | `-A` | **Aggressive Scan** — OS + version + scripts + traceroute |
| 30-33 | `-p` | **Specific Ports** — scan only user-specified ports |

---

## 📝 Sample I/O

```
Enter choice: 2
Enter target IP: 192.168.1.1
Command: nmap -sT 192.168.1.1
```

---

## ⚠️ Attacks & Defenses

| Attack | Defense |
|--------|---------|
| Port Scanning → find vulnerable services | Firewall rules, close unused ports |
| OS Fingerprinting → tailor exploits | IDS/IPS (Snort, Suricata) |
| Stealth/Xmas Scans → evade detection | Rate limiting, honeypots |

> ⚠️ Scanning without permission is **illegal**. Always get written authorization.
