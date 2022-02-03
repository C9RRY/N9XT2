# Project to simplify the management of the repair shop 
  

## Install
git clone https://github.com/C9RRY/N9XT2.git
cd N9XT2
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


## How to run
cd fix_store
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
