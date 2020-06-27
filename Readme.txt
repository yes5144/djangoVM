## project djangoVM start

### clone and start
git clone https://github.com/yes5144/djangoVM.git
cd djangoVM
pip install -r requirements.txt

python manage.py  makemigrations
python manage.py  migrate
python manage.py  runserver