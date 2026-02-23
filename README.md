# Secure Notes - Django Project

Secure Notes is a Django-based web application that allows users to create and store encrypted notes securely using AES-256-GCM encryption.

---

## Features

- User Registration & Login
- Password Hashing (Django built-in)
- AES-256-GCM Encrypted Notes
- Simple and clean UI

---

##  Requirements

- Python 3.10 or higher
- pip (Python package manager)
- Git

---

## ⚙️ How to Install and Run the Project Locally

### 1. Clone the Repository
``` bash
git clone https://github.com/zhdipto/secure-notes.git
cd secure-notes
```
### 2. Create and Activate a Virtual Environment
```
python3 -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5. Start the Development Server
```
python manage.py runserver
```
### how to see encryption on database
You can open the database file (`db.sqlite3`) using external tools such as:
- SQLite extension in VS Code
#### Steps:
1. Install SQLite extension in VS Code
2. Open the application
3. Select the `db.sqlite3` file
4. Browse the tables to view stored data (`users_user and users_securenote`)
