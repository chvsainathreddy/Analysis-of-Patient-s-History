
# 🧠 Healnalyzr – Smart Patient History Analysis System

## 🧬 About Healnalyzr

Healnalyzr is an intelligent system designed to assist healthcare professionals and researchers by providing a streamlined approach to analyzing a patient’s medical history. Its core functionalities include:

- **Patient History Analysis:** Automatically extract patterns, trends, and anomalies in historical medical records.
- **Clinical Decision Support:** Aid physicians by highlighting potential health risks or recurring symptoms.
- **Secure Data Management:** Ensures medical records are processed and handled with high standards of data protection and privacy.
- **Interoperability:** Can be extended or integrated with Electronic Health Record (EHR) systems, improving healthcare workflows.
- **Deployment Ready:** Built to be lightweight and easily deployable on cloud platforms like Heroku using the provided `Procfile`.

This tool is ideal for:
- Clinics and hospitals seeking analytical tools for patient record evaluation.
- Researchers working on healthcare data projects.
- Health-tech startups looking to integrate ML or analytics on patient data.

Whether you're aiming to detect early signs of chronic illness or just want a cleaner way to analyze and store patient records, Healnalyzr is built to scale and adapt.

## 🔧 Project Structure

- `run.py` – Main application entry point.
- `requirements.txt` – Python dependencies for the project.
- `Procfile` – Used for deployment (e.g., Heroku).
- `history/` – Contains patient history and related tools.
- `.git/` – Git version control directory.


## 🛠️ Tech Stack

- **Programming Language:** Python 3
- **Web Framework:** Flask
- **Data Handling:** SQLite
- **Deployment:** Heroku (via `Procfile`)
- **Version Control:** Git


## 🚀 How to Run

1. Clone the repository or download the project files.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python run.py
   ```

## 📦 Deployment

The `Procfile` suggests the project is ready for deployment on platforms like Heroku.

## 💡 Features

- Analyze patient history and medical data.
- Python-powered backend.
- Easily deployable.

## 📁 Directory Overview

```
Healnalyzr/
├── history/                # Core logic and database handling
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── history.db          # Local SQLite database
│   └── templates/          # HTML templates for UI
├── run.py               # Main executable script
├── requirements.txt     # Python dependencies
├── Procfile             # Deployment process descriptor
├── .git/                # Git metadata (if applicable)
```

## 🧪 Requirements

Python 3.7+

## 📜 License

For Educational Purpose

---

*Crafted for efficient medical history analysis.* 🩺
