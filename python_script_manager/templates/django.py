def django_oninit():
    pass


django = {
    "body": {
        "scripts": {
            "start": {
                "command": "python manage.py runserver",
                "description": "Run Django server"
            },
            "mig": {
                "command": "python manage.py migrate",
                "description": "Migrate database"
            },
            "mkmig": {
                "command": "python manage.py makemigrations",
                "description": "Make migrations"
            }
        }
    },
    "config": {
        "events": {
            "oninit": django_oninit
        }
    }
}
