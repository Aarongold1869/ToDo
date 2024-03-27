# ToDo Application Tutorial with Django and HTMX

## Front-end setup
1. create an html template - This will be the main html template used by the application

## Application Setup
2. create and launch virtual environment with django (pipenv)
    
    `pip install pipenv`

    `pipenv install django`

    `pipenv shell`

    `django-admin startproject todo .`

3. configure application settings
4. migrate database 

    `python manage.py migrate`

5. create superuser 

    `python manage.py createsuperuser`

6. run application server 

    `python manage.py runserver`

7. configure and collect static files 

    `python manage.py collectstatic`

## Application Development
8. create todo view
9. create a url path 
10. update template 
11. create a model 
12. configure HTMX

    CDN: 

    `<script src="https://unpkg.com/htmx.org@1.9.11" integrity="sha384-0gxUXCCR8yv9FM2b+U3FDbsKthCI66oH5IA9fHppQq9DDMHuMauqq1ZHBpJxQ0J0" crossorigin="anonymous"></script>`

    django-htmx lib 

    `pip install django-htmx`

    settings.py apps

    `INSTALLED_APPS = [..., "django_htmx", ...,]`

    settings.py middleware

    `MIDDLEWARE = [ ..., "django_htmx.middleware.HtmxMiddleware", ..., ]`

    base.html 

    `hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'`

13. Create CRUD views 

    - [ ] Create
    - [x] Retrieve 
    - [ ] ~~update~~
    - [ ] destroy

## You did it!