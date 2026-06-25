🔐 Password Tool

A simple and secure console password generator written in Python.

This tool can generate:

🔑 Random passwords
📝 Word-based passphrases
📋 Automatic clipboard copying

---

✨ Features
Password Generator

Generate secure passwords with customizable options:

Numbers (0-9)
Letters (a-z, A-Z)
Symbols (!@#$%^&*...)
Custom password length

Example:

J#7z!2QkP@8xW4nR

---

Passphrase Generator

Generate memorable passwords from a word list file.

Example:

apple-ocean-mountain-coffee

Features:

Custom separator
Random word selection
Support for large wordlists

---

Clipboard Support

Generated passwords are automatically copied to your clipboard using pyperclip.

[✓] Password generated successfully.
[✓] Copied to clipboard.

---

📦 Requirements
Python 3.10+
pyperclip

Install dependencies:

pip install pyperclip

---

🚀 Usage

Run the program:

python password-generator.py

Main menu:
```
========================
 PASSWORD TOOL
========================
[1] Start password generation
[2] Generate passphrase
[3] Exit
```

---

🔧 Password Generator Options
```
========================
 OPTIONS
========================
[1] Numbers: ON
[2] Letters: OFF
[3] Symbols: OFF
[4] Password length: 100
[5] Generate password
[6] Back to menu
```

You can enable or disable character types before generating a password.

---

📖 Passphrase Generator

Prepare a text file containing words:

apple
ocean
mountain
coffee
winter
sunrise

Select the file path and choose:

Number of words
Separator (space, -, _, etc.)

Generated result:

coffee-sunrise-apple-mountain

---

📁 Project Structure
```
password-tool/
│
├── main.py
├── wordlist.txt
└── README.md
```

---

📄 License

This project is open source and available under the MIT License.

Made with ❤️ and Python.
