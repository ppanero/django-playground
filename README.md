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

4. Stop server and run migrations if needed

```shell
$ python manage.py migrate
# if needed, can create only polls app migrations
$ python manage.py makemigrations polls
```

5. Add superuser

```shell
$ python manage.py createsuperuser
```

## Notes

- Support for URL patters, naming/namespacing and reversing (get absolute URL).
- Support for ASGI and WSGI
- Can test migrations with `manage.py check`
- Can see the SQL statements of migrations by checking using the `manage.py sqlmigrate` manage command
- Can open a shel with `manage.py shell`

## Questions

**URL Dispatcher**

- How would it behave with a path converter if it's not the last one. For example". Idea: might require a custom converter or a regex which ignores integers (assumes the path does not have integers).

```python
from django.urls import path

urlpatterns = [
    path("some/<path>/<int:more_info>/", ...),
]

# What would be the arguments passed for a request to
# `some/test/path/to/folder/1234/`
```

## Glossary

- _Project_ vs _App_: an app is ~ a django specific library, and a project might include
many of them (plus configuration, etc.).