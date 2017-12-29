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
 * If standing up the frontend too - confirm `proxy` is set correctly in `package.json`

If using local (non-prod) database
```
python manage.py migrate
```

Start service
```
python manage.py runserver
```
