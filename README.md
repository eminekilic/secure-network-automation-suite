# 🛡️ Secure Network Backup Automation Tool

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Cisco](https://img.shields.io/badge/Network-Cisco_IOS-black?style=for-the-badge&logo=cisco&logoColor=white)
![Security](https://img.shields.io/badge/Security-DotEnv-green?style=for-the-badge)

A robust, secure, and automated Python tool designed to backup **Cisco IOS configurations** for multiple devices simultaneously. This project bridges the gap between traditional Network Engineering and modern **NetDevOps** practices by implementing secure coding standards.

## 🚀 Key Features

* **🔒 Security First:** Uses environment variables (`.env`) to isolate sensitive credentials (IP, Username, Password) from the source code, adhering to "Security by Design" principles.
* **⚡ Multi-Device Support:** Reads device inventory from a CSV file, allowing the script to scale from 1 to 1000+ devices without code changes.
* **🛡️ Error Handling:** Includes robust exception handling. If one device fails (e.g., connection refused), the script logs the error and continues to the next device.
* **📝 Automated Logging:** Saves `running-config` with dynamic timestamped filenames for easy archiving.

## 🛠️ Architecture & Technologies

* **Language:** Python 3.12
* **Libraries:** `Netmiko` (SSH Handling), `csv` (Inventory Management), `datetime`
* **Lab Environment:** EVE-NG (Cisco IOL Images)
* **Protocol:** SSH (Port 22)

## ⚙️ Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/eminekilic/secure-cisco-backup.git](https://github.com/eminekilic/secure-cisco-backup.git)
    cd secure-cisco-backup
    ```

2.  **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Inventory (CSV)**
    * Open `inventory.csv` and add your devices in the following format:
    ```csv
    device_name,ip_address,username,password,device_type
    R1,192.168.125.150,admin,cisco,cisco_ios
    R2,192.168.125.151,admin,cisco,cisco_ios
    ```

4.  **Run the Script**
    ```bash
    python multi_backup.py
    ```

## 📂 File Structure

```text
.
├── multi_backup.py      # Main automation script (Loops through CSV)
├── inventory.csv        # Device list (IPs, Credentials)
├── inventory.example.csv # Template for inventory (Safe to upload)
├── .gitignore           # Git configuration (Hides sensitive files)
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

## 🔮 Future Improvements

- [ ] Multi-threading for backing up multiple devices simultaneously.
- [ ] Integration with Slack/Teams for notification.
- [ ] AI-based Anomaly Detection (Integrating LSTM models).

---
*Developed by **Emine Kılıç** - Computer Engineer & Network Automation Enthusiast*