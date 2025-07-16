# 🔐 Password Manager with Generator

A simple GUI-based password manager built with Python. It includes:
- Secure password generator
- Password storage (locally in JSON)
- Basic search and listing interface

---

## 🧩 Features

- Generate secure passwords
- Store passwords with website, username, and notes
- Save/load from local file
- GUI built with `tkinter`


---

## 🚀 Installation

1. Clone the repo:

git clone https://github.com/OnePieceExsists/password_manager.git
cd password-manager

# Install requirements(Optional):

python -m venv venv
.\venv\Scripts\Activate.ps1
# source venv/bin/activate (Linux, macOS)


# Run the app:

python main.py


# Testing
*Unit tests for password generation and data storage:

python -m unittest discover tests/


# Project Structure

password_manager/
│
├── main.py
├── password_generator.py
├── password_manager.py
├── gui.py
├── storage.json          # file to store passwords
├── LICENSE               # license file with Apache-2.0 text
├── README.md
└── tests/
    ├── test_password_generator.py
    └── test_password_manager.py


# 🖥️ Screenshots

![Password Manager Screenshot](screen/pass_manager_prscr.png)

# 🔐 Security Notes
Passwords are stored in plain JSON, without encryption.

For real-world use, consider:

Master password or login

Encryption (e.g., using Fernet / AES)

Secure storage (e.g., encrypted database or keyring)

# 📌 Requirements
Python 3.8+

Tkinter (usually preinstalled)

# ✅ To-Do / Future Features
 Add master password / login ✅

 Encrypt stored passwords ✅

 Add password strength indicator

 Export/import entries

 Cross-platform packaging (e.g., EXE with PyInstaller)

# 📄 License
This project is licensed under the Apache License 2.0.
You may use, modify, and distribute it in compliance with the Apache 2.0 License.
