# ELLIOT SOCIAL

<div align="center">

# ELLIOT SOCIAL

### Social Intelligence & Public-Source Research

**A Python-powered CLI for organized social profile research and information management.**

Explore public information. Organize research. Keep your workflow simple.

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-6C5CE7?style=flat-square)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

[Features](#-features) · [Installation](#-installation) · [Configuration](#-mongodb-setup) · [Usage](#-usage)

</div>

---

## ✨ Features

- **CLI Interface** — terminal-based workflow with colorful output.
- **Public-Source Research** — organize permitted public profile information.
- **MongoDB Integration** — store supported research records in a database.
- **Interactive Setup** — configure your MongoDB connection through `setup.py`.
- **Environment Configuration** — keep connection credentials in a local `.env` file.
- **Python-Based** — straightforward setup and extensible project structure.

## 🧰 Built With

| Technology | Purpose |
|---|---|
| Python | Core application |
| Colorama | Terminal colors |
| PyMongo | MongoDB connection |
| python-dotenv | Environment configuration |
| MongoDB | Data storage |

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Elliotcrown/SOCIALPY.git
cd SOCIALPY
```

Create and activate a virtual environment on Linux/Kali:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install colorama pymongo dnspython python-dotenv
```

## 🗄️ MongoDB Setup

Start the interactive configuration:

```bash
python setup.py
```

Follow the prompts to configure your MongoDB URI.

The connection string is saved in your local `.env` file. Keep this file private and never commit it to GitHub.

> Each user must configure an authorized MongoDB connection. A local setup script does not automatically create a secure shared database for every repository user.

## 🚀 Usage

Once the database is configured, run:

```bash
python main.py
```

Follow the options displayed in the terminal.

## 🔐 Responsible Use

- Research only information you are authorized to access.
- Respect privacy, applicable laws, and platform terms.
- Never collect or store social media passwords.
- Keep database credentials and secret keys out of source control.
- Use appropriate database permissions and access controls.

## 🗺️ Project Structure

```text
SOCIALPY/
├── main.py
├── setup.py
├── db/
│   └── instagram_db.py
├── platforms/
│   └── instagram.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Adjust this tree to match your actual repository files.*

## 👨‍💻 Author

**ELLIOTCROWN**

GitHub: [@Elliotcrown](https://github.com/Elliotcrown)

Project: [ELLIOT SOCIAL — SOCIALPY](https://github.com/Elliotcrown/SOCIALPY)

## 📄 License

This project is distributed under the MIT License if the repository includes an applicable MIT `LICENSE` file.

---

<div align="center">

### ELLIOT SOCIAL

**Research Smart. Stay Responsible.**

</div>
