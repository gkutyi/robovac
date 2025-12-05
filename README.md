# Robovac – L60 / L60 SES Support (Home Assistant Integration)

This is a **patched & simplified Robovac integration**, updated to support:

✔ Eufy **L60 / L60 SES (T2277)**  
✔ Battery sensor  
✔ Online/offline status  
✔ HACS installation  
❌ Robovac control features (start/stop, navigation, maps) — *not possible because L60 uses the new Eufy Clean API*

---

## Installation via HACS

1. Open **HACS → Integrations**
2. Click **⋮ → Custom repositories**
3. Add: https://github.com/gkutyi/robovac
4. Category: **Integration**
5. Install & restart Home Assistant
6. Add integration: **Settings → Devices → Add Integration → Robovac**

---

## Configuration

You will be prompted for:

| Field | Description |
|-------|-------------|
| Name | Friendly name |
| ID | Device ID (from Eufy App) |
| Model | Must be **T2277** |
| IP Address | Local IP of the robot |
| Access Token | Token obtained via API dump |

The integration performs:

- Model validation  
- TCP connectivity test  
- Local storage of credentials  

---

## Supported Models

| Model | Status |
|--------|--------|
| **T2277 – Eufy L60/L60 SES** | ✔ Sensors supported |
| other Robovac models | ❌ Not supported in this fork |

---

## Features

### Available:
- Battery percentage  
- Connectivity availability  
- HACS compatibility  
- UI config flow

### Not available:
- Cleaning controls  
- Docking  
- Maps  
- Suction power  
- Room navigation  

Reason: L60 uses **Eufy Clean Cloud API**, not Tuya Local.

---

## File structure

custom_components/robovac/

│── init.py
│── manifest.json
│── config_flow.py
│── const.py
│── sensor.py
└── coordinator.py

---

## Disclaimer

This project is maintained by the community and is not affiliated with Anker/Eufy.
