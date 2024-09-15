command:
python manage.py makemigrations - Generates migration files for model changes
python manage.py migrate        - Applies migrations to update the database schema
python manage.py showmigrations - to display the current status of all migrations 
python manage.py runserver      - Starts the Django development server http://127.0.0.1:8000/.
.\env\Scripts\Activate          - to activate Virtual Environment



Django Project Folder Structure
project/
│
├── manage.py                # Command-line utility for managing the project
├── project/                 # Main project directory
│   ├── __init__.py          # Marks the directory as a Python package
│   ├── settings.py          # Main configuration file for the project (database, middleware, apps)
│   ├── urls.py              # URL routing for the project
│   ├── asgi.py              # ASGI configuration (for asynchronous support)
│   └── wsgi.py              # WSGI configuration (for deployment with WSGI servers)
│
├── app/                 # Application-specific directory
│   ├── migrations/          # Stores migration files for database changes
│   ├── __init__.py          # Marks the directory as a Python package
│   ├── admin.py             # Admin panel configuration for the app
│   ├── apps.py              # App configuration file
│   ├── models.py            # Defines the database models (tables)
│   ├── views.py             # Contains logic to process requests and return responses
│   ├── tests.py             # Contains unit tests for the app
│   ├── urls.py              # App-specific URL routing (if needed)
│   └── templates/           # HTML templates for the app (optional, manually created)
│       └── appname/         # Folder that stores templates for the app
│
├── static/                  # Static files (CSS, JavaScript, images) (optional, manually created)
│
└── media/                   # Media files (user-uploaded files, like images) (optional, manually created)
