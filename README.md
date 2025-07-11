# Django Polls App

A simple, modern web application for creating and voting on polls, built with Django and styled using Bootstrap.

## Features
- Create, edit, and delete polls and choices (admin interface)
- Vote on polls and view real-time results
- Responsive design with Bootstrap
- Custom background image and styles

## Quick Start

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd mypoll
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
7. **Access the app:**
   - Polls: http://127.0.0.1:8000/polls/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure
```
mypoll/
├── manage.py
├── mysite/
│   └── ...
├── polls/
│   ├── admin.py
│   ├── models.py
│   ├── static/
│   │   └── polls/
│   │       ├── style.css
│   │       └── images/
│   ├── templates/
│   │   └── polls/
│   │       ├── detail.html
│   │       ├── index.html
│   │       └── results.html
│   └── ...
├── requirements.txt
└── README.md
```

## License
MIT
