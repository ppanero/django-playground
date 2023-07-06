# django-playground
Just playing with Django


1. Install

```shell
$ pip install django
$ python -m django --version
```

2. Bootstrap a Django project

```shell
# create project
$ django-admin startproject playground
# get into the project
$ cd playground/
# create app
$ python manage.py startapp polls
```

3. Start server

```shell
# in playground/
$ python manage.py runserver <HOST>:<PORT>
```

## Glossary

- _Project_ vs _App_: an app is ~ a django specific library, and a project might include
many of them (plus configuration, etc.).