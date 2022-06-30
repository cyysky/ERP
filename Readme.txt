pip install -r requirements.txt

cd ERP

python manage.py migrate

python manage.py migrate --run-syncdb

python manage.py createsuperuser --username=admin

python manage.py runserver 0.0.0.0:8000

