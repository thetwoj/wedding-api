# wedding-api

Install dependencies
```
pip install django
pip install djangorestframework
pip install drf-nested-routers
pip install mysqlclient
```

 * Pull `settings.py` from the prod server
 * Add `localhost` to `ALLOWED_HOSTS`
 * Disable `SECURE_SSL_REDIRECT`

Create database (if using local database)
```
python manage.py migrate
```

Start service
```
python manage.py runserver
```
