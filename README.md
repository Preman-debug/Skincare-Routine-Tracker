# Skincare Routine Tracker

## 📌 Project Description
The Skincare Routine Tracker is a console-based web application built with Flask that helps users track their daily skincare routine, monitor product usage, and observe progress over time. Users can log products, record usage, and provide feedback to track effectiveness.

## 🚀 Features
- Add and manage skincare products with frequency and purpose.
- Log daily usage of products along with user feedback.
- View progress reports to track improvements over time.

## 🛠️ Technologies Used
- Python (Flask Framework)
- SQLite (Database for storing product and usage data)
- HTML, CSS (Frontend Templates)

## 📂 Folder Structure
```
skincare_tracker/
│── app.py                 # Main Flask application
│── skincare.db             # SQLite database (auto-created)
│── requirements.txt        # Dependencies
│── templates/              # HTML templates
│   │── index.html          # Home page
│   └── progress.html       # Progress tracking page
└── static/                 # Static files (CSS, JS, Images)
    └── style.css           # CSS file for styling
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/skincare-tracker.git
cd skincare-tracker
```
### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Run the Application
```sh
python app.py
```
Access the application at `http://127.0.0.1:5000/`



