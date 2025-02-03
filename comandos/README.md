Criando o ambiente virtual e instação do Django

python -m venv venv
venv/Scripts/activate
pip install django 
django-admin startproject myproject
python manage.py startapp products

Criação do models e migrações

python manage.py makemigrations 
python manage,py migrate