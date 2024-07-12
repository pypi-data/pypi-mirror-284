# django-access-timer-middleware

Access timer middleware is a middleware which allow to control access to some paths, like
/api/, /admin/ and what you want!


## How to install the package

To install the package, run:

```bash
pip install django-access-timer-middleware
```
In settings.py write next stuff:

INSTALLED_APPS:
```python
INSTALLED_APPS = [
    ...,
    'access_timer_middleware',
    ...,
]
```

MIDDLEWARE:
```python
MIDDLEWARE = [
    ...,
    'access_timer_middleware.middleware.AccessTimerMiddleware',
]
```

And then:

```bash
python manage.py makemigrations
python manage.py migrate
```
## description

The default access time to endpoints is 1 hour. <br/>
After expiring access time you won't get some endpoint, then you will receive error 403.<br/>
That value you can change in admin panel.
Available the next values:
<ul>
    <li>1 hour</li>
    <li>3 hours</li>
    <li>6 hours</li>
    <li>1 day</li>
    <li>2 weeks</li>
</ul>

## How to use?

In settings.py you should to set a one of two constants:



```python
RESTRICTED_PATHS = ['/api/']
```
The paths are participating in checking access

or...

```python
EXCLUDED_PATHS = ['/api/stuff/login/', '/api/stuff/signup/', '/admin/']
```
...paths, which are excluded from it, but rest of the endpoints there are in checking.

Using those two constants at the same time will throw an exception.


## Version

Current version: 1.1

## Updates

This package won't have updates, except of bug updates.

## Author

pavelbeard