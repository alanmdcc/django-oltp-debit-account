# Django OLTP - Debit Account

Alan Martin del Campo

Install dependencies
```
pip install -r requirements.txt
```

Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

Create a super user to interact with admin interface (Optional)
```
python manage.py createsuperuser
```

Start server (default port: 8000)
```
python manage.py runserver $PORT
```

Path for admin management
```
localhost:$PORT/admin/
```

Path to see all available paths
```
localhost:$PORT/api/
```