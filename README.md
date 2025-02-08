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

## 🔥 Usage Guide
1. Open the web application.
2. Add your skincare products with details like name, frequency, and purpose.
3. Log usage daily and provide feedback.
4. View progress in the **Progress Tracking** section.

## 💡 Contributing
Feel free to fork this repository and contribute by submitting a pull request.
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a Pull Request on GitHub.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any issues, please raise a GitHub issue or reach out via email at `your-email@example.com`.

