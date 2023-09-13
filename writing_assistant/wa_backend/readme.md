# how to run
## create environment 
```angular2html
# 创建
conda create -n YOUR_ENVIRONMENT_NAME python=3.9.16
# 激活
conda activate YOUR_ENVIRONMENT_NAME
```
## install dependance
```angular2html
pip install -r requirements.txt
```

## initialize 
```angular2html
# 数据库创建和迁移
python manage.py makemigrations writing_assistant_backend
python manage.py migrate
```

## run
```angular2html
python manage.py runserver localhost:50000
```
