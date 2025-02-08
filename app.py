from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('skincare.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            frequency TEXT NOT NULL,
            purpose TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            date TEXT,
            feedback TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('skincare.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    frequency = request.form['frequency']
    purpose = request.form['purpose']
    conn = sqlite3.connect('skincare.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, frequency, purpose) VALUES (?, ?, ?)", (name, frequency, purpose))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/log_usage', methods=['POST'])
def log_usage():
    product_id = request.form['product_id']
    feedback = request.form['feedback']
    date = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect('skincare.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usage (product_id, date, feedback) VALUES (?, ?, ?)", (product_id, date, feedback))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/progress')
def progress():
    conn = sqlite3.connect('skincare.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT products.name, usage.date, usage.feedback FROM usage
        JOIN products ON usage.product_id = products.id
        ORDER BY usage.date DESC
    ''')
    progress_data = cursor.fetchall()
    conn.close()
    return render_template('progress.html', progress_data=progress_data)

if __name__ == '__main__':
    app.run(debug=True)
