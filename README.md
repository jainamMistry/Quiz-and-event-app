## 📌 Overview

This app allows users to:
- Browse and take quizzes with dynamic questions.
- Submit answers and see their results.
- View upcoming events with details like date and location.

Admins can manage quizzes, questions, answers, and events via the Django admin panel.

---

## ✨ Features

### **For Users**
- **Quizzes**:
  - List all available quizzes.
  - Take quizzes and get instant results.
  - Review correct/incorrect answers.
- **Events**:
  - See a list of upcoming events.
- **UI**:
  - Responsive design with **Tailwind CSS**.
  - Works on mobile and desktop.

### **For Admins**
- Add, edit, or delete quizzes, questions, answers, and events.
- View user submissions and scores.

---

## 🛠 Tech Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite
- **Frontend**: HTML + Tailwind CSS
- **Python**: 3.13+

---

## 📁 Project Structure

quiz_events/
├── quiz_events/          # Main project settings and URLs
├── quizzes/              # Quiz app (models, views, admin)
├── events/               # Events app (models, views, admin)
├── templates/            # HTML templates
│   ├── base.html         # Base layout
│   ├── home.html         # Home page
│   ├── quizzes/          # Quiz-related pages
│   └── events/           # Events page
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
Copy

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Navigate to the project directory**:
   ```bash
   cd C:\Users\JAINAM MISTRY\OneDrive\Documents\django\quiz_events



(Optional) Create a virtual environment:
bash
Copy

python -m venv venv
venv\Scripts\activate  # Windows



Install Django:
bash
Copy

pip install django



Run migrations:
bash
Copy

python manage.py migrate



(Optional) Create sample data:
bash
Copy

python manage.py create_sample_data

This adds 3 sample quizzes and 4 events.


(Optional) Create an admin account:
bash
Copy

python manage.py createsuperuser



Start the server:
bash
Copy

python manage.py runserver



Open the app:

Home: http://127.0.0.1:8000/
Quizzes: http://127.0.0.1:8000/quizzes/
Events: http://127.0.0.1:8000/events/
Admin: http://127.0.0.1:8000/admin/


📖 Usage
For Users


Take a Quiz:

Go to the Quizzes page.
Click Start Quiz on any quiz.
Enter your name and answer the questions.
Submit to see your score and review answers.


View Events:

Go to the Events page.
See all upcoming events with dates and locations.

For Admins


Add a Quiz:

Log in to the admin panel.
Go to Quizzes and click Add Quiz.
Add questions and answers.


Add an Event:

Go to Events in the admin panel.
Click Add Event and fill in the details.


📝 Key Features

Dynamic Quizzes: Questions are loaded from the database.
Score Calculation: Automatic scoring on submission.
Responsive UI: Works on all devices.

🔧 Management Commands

Create Sample Data:
bash
Copy

python manage.py create_sample_data

Adds sample quizzes and events for testing.
