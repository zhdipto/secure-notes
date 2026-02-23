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

## How to Install and Run the Project Locally

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
## How to see encryption on database
You can open the database file (`db.sqlite3`) using external tools such as:
- SQLite extension in VS Code
- DB Browser for SQLite
#### Steps:
1. Install SQLite extension in VS Code
2. Open the application
3. Select the `db.sqlite3` file
4. Browse the tables to view stored data (`users_user and users_securenote`)


## Demo Screenshot
<img width="1920" height="1080" alt="Screenshot from 2026-02-24 02-27-21" src="https://github.com/user-attachments/assets/d20dff84-23cc-4bd0-8523-d5e97f163214" />
<img width="1920" height="1080" alt="Screenshot from 2026-02-24 02-27-30" src="https://github.com/user-attachments/assets/c4b5d753-6bb5-4b6a-a134-d8c7539d237f" />
<img width="1920" height="1080" alt="Screenshot from 2026-02-24 02-27-36" src="https://github.com/user-attachments/assets/1e39dcb8-e49a-4930-8d05-969d69874d40" />
<img width="1920" height="1080" alt="Screenshot from 2026-02-24 02-27-42" src="https://github.com/user-attachments/assets/a1c8c2d0-50b8-4c11-a109-dbac19eb6264" />

## Encrypted content Screenshot
<img width="1920" height="1080" alt="Screenshot from 2026-02-24 02-29-27" src="https://github.com/user-attachments/assets/1dc90c07-c81a-47b9-b126-163a714119a5" />
<img width="1920" height="1080" alt="Screenshot from 2026-02-24 02-29-36" src="https://github.com/user-attachments/assets/e3e7d68c-8d87-4fcc-a30d-21b951acd9e1" />
