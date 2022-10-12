cd /d %~dp0
cd ERP
python manage.py makemigrations                    
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py runserver  0.0.0.0:8000
