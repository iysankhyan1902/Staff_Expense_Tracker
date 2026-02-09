💰 Expense Tracker Application

🧾 Overview

A Django-based expense tracker application that allows users to record, manage, and track expenses through a structured dashboard using forms and database models.

🎯 Objective

To build a simple and efficient system for tracking expenses while practicing Django CRUD operations, forms, and project architecture.

⚙️ Features

- Add, update, and delete expense records
- Form-based expense entry with validation
- View expense details in a centralized dashboard
- Django Admin integration for backend management
- Persistent storage using SQLite


🛠 Tech Stack

Backend: Python, Django
Frontend: HTML, CSS
Database: SQLite
Tools: Git, GitHub

## 📂 Project Structure

```bash
expense-tracker/
├── manage.py
├── staffdashboard/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── staffapp/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── admin.py
│   └── migrations/
├── templates/
```
🚀 How to Run Locally
- git clone <repo-url>
- cd expense-tracker
- python -m venv venv
- venv\Scripts\activate
- python manage.py migrate
- python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

🧠 Learning Outcomes

- Implemented CRUD operations using Django models and forms
- Worked with Django MVT architecture
- Gained experience in form validation and database migrations
- Improved understanding of project structuring and version control
