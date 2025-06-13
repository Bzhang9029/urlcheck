# 🔎 URL Checker

A simple desktop application to scan URLs for **malicious**, **suspicious**, or **harmless** content using the [VirusTotal API](https://www.virustotal.com/). Built with **Python** and **PyQt5**, it provides a clean GUI to help users assess the safety of URLs quickly.

---

## ✅ Features

- 🛡️ Scan URLs using VirusTotal’s real-time threat intelligence  
- 🧠 Categorizes results as **Harmless**, **Suspicious**, or **Malicious**  
- ⚡ Lightweight GUI using PyQt5  
- 📋 One-click scan and result display  

---

## 🚀 Installation

### Prerequisites

- Python 3.x  
- pip  
- A [VirusTotal API key](https://www.virustotal.com/gui/join-us)

### Install Dependencies

```bash
pip install -r requirements.txt
````

If you don’t have a `requirements.txt` yet, you can create one:

```bash
pip freeze > requirements.txt
```

---

## 🔧 Setup

Open `VirusTotalClient.py` and add your API key:

```python
API_KEY = "your_virustotal_api_key_here"
```

---

## 🧪 Run the App

```bash
python main.py
```

---

## 🛠 Technologies Used

* Python
* PyQt5
* VirusTotal Public API

---

## 📁 Project Structure

```
url-checker/
├── main.py               # PyQt5 GUI app
├── VirusTotalClient.py   # Handles API requests
├── README.md             # Project documentation
└── .gitignore            # Optional: Python ignores
```

---

## 🙋‍♂️ Author

Brian Zhang
[@Bzhang9029](https://github.com/Bzhang9029)

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 📌 Next Steps

1. Copy this into your `README.md`
2. Save it
3. Run:

```bash
git add README.md
git commit -m "Add full README with usage and features"
git push origin main
```

