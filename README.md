# 🔐 Secure File Transfer Application – CodeAlpha Internship

This project is part of the **Cybersecurity Internship** at **CodeAlpha**.  
It allows secure transfer of files using **AES encryption**, user authentication, and logs all actions for audit purposes.

---

## 💡 Features

- 🔐 **End-to-End Encryption** (AES)
- 👤 **User Authentication** (Login/Register with password hashing)
- 🗂️ **File Encryption & Decryption** via GUI
- 📜 **Audit Logging** (Tracks file transfers, login events)
- 🧾 Easy-to-use **Tkinter GUI**
- 🛡️ Implements basic **access control**

---

## 🛠️ Tech Stack

- Python 3
- `tkinter` – GUI
- `cryptography` – AES encryption
- `hashlib` – Password hashing (SHA-256)
- `json` – User storage
- `os`, `datetime` – File system & logging

---

## 📁 Folder Structure

SecureFileTransfer/
├── main.py # GUI and app logic
├── auth.py # Login/registration
├── encryption.py # AES encryption/decryption
├── users.json # Stores registered users
├── transferred_files/ # Encrypted/decrypted files
├── logs/
│ └── audit.log # Tracks actions
└── README.md # This file

yaml
Copy code

---

## 🚀 How to Run

1. **Install Requirements:**
   ```bash
   pip install cryptography
2. Run the App:
   ```bash
   python main.py
3. Use the GUI to:

Register or Login

Encrypt a file

Decrypt an encrypted file

Encrypted files will be saved in /transferred_files/.
