# urlcheck
# 🔎 URL Checker

A simple desktop application to scan URLs for malicious, suspicious, or harmless content using the [VirusTotal API](https://www.virustotal.com/). Built with **Python** and **PyQt5**, it provides a clean GUI to help users assess the safety of URLs quickly.

---

## ✅ Features

- 🛡️ Scans URLs using VirusTotal’s real-time threat intelligence
- 🧠 Categorizes results as **Harmless**, **Suspicious**, or **Malicious**
- ⚡ Lightweight GUI using PyQt5
- 📋 Simple one-click scan and response display

## 🚀 Installation

### Prerequisites

- Python 3.x
- pip
- A VirusTotal API key

### Install dependencies

```bash
pip install -r requirements.txt
If you don’t have a requirements.txt yet, you can create one with:

bash
Copy
Edit
pip freeze > requirements.txt
🔧 Setup
Add your VirusTotal API key in VirusTotalClient.py:
API_KEY = "your_virustotal_api_key_here"

🧪 Run the App
python main.py

### 🛠 Technologies Used
Python
PyQt5
VirusTotal Public API

###📁 Project Structure
bash
Copy
Edit
url-checker/
├── main.py                # PyQt5 GUI app
├── VirusTotalClient.py    # Handles API requests
├── README.md              # Project documentation
└── .gitignore             # Optional: Python ignores
🙋‍♂️ Author
Brian Zhang
@Bzhang9029

📄 License
MIT License. See LICENSE for details.


### 📌 Next Steps:

1. Copy this into your `README.md`
2. Save it
3. Run:

```bash
git add README.md
git commit -m "Add full README with usage and features"
git push origin main










