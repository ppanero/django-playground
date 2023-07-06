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

### Database

- Supports multi-database (e.g. primary, replicas, etc.). Provides hints for routing and
supports custom router classes.
    - No cross-database FK support.
- Django ORM implements Active Record pattern, while SQLAlchemy implements Data Mapper.

**Models**

- Model inheritance resolves to two tables linked with a 1to1 relation.
- `Meta` is not exposed to children classes.
- `select_related` (SQL join) vs `prefech_related` (Python join), see [more](https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related).
- Complex filters with `Q` and operators (&, |, etc.).
- Can log SQL queries by [configuring the backend](https://docs.djangoproject.com/en/2.1/topics/logging/#django-db-backends).

**Transactions**

- Runs in `autocommit` by default.
- Can tie a transaction per request by setting.
`ATOMIC_REQUESTS`, if there is an exception the transaction is rolledback. Careful on-high
load since there is 1 transaction open per request.
- Can also control transactions manually (begin, nesting, commit, etc.).
- `@atomic` checks the exit code to rollback/commit, so don't catch exceptions inside to
avoid unpredictable behavior.
- If there is a rollback the model state needs to be "undone" manually.
- Callbacks (e.g. mails) are post-transaction so they do not affect data persistence.

**Optimizations**

- Callables (e.g. `.all()`, `.one()`) will always cause a lookup, assign the item to a
memory instance to cache it (e.g. `test = model.all()`).
- Profit from database (duh!): query columns with `unique`, or `indexed`.
- Pre-fetch related if they are needed (FKs).
- Use fk (e.g. `blog.creator_id`) rather than the reference object
(e.g. `blog.creator.id`).
- Use bulk methods when sensitively possible.


### URL Dispatcher

- Support for URL patters, naming/namespacing and reversing (get absolute URL).

### CLI

- Can test migrations with `manage.py check`.
- Can see the SQL statements of migrations by checking using the `manage.py sqlmigrate`
manage command.
- Can open a shel with `manage.py shell`.

### Deployment

- Support for ASGI and WSGI.

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

**Models**

- Model inheritance resolves to a 1to1 FK. When resolving an obj (i.e. `SELECT`) does it
imply a `JOIN`?

## Glossary

- _Project_ vs _App_: an app is ~ a django specific library, and a project might include
many of them (plus configuration, etc.).



TBC from https://docs.djangoproject.com/en/4.2/intro/tutorial03/