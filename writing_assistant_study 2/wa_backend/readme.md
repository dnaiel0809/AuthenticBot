# how to run
## create a virtual environment 
```angular2html

conda create -n YOUR_ENVIRONMENT_NAME python=3.9.16

conda activate YOUR_ENVIRONMENT_NAME
```
## install dependence
```angular2html
pip install -r requirements.txt
```

## initialize
```angular2html
python manage.py makemigrations writing_assistant_backend
python manage.py migrate
```

## run
```angular2html
python manage.py runserver localhost:50000
```
