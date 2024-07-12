# django-newsingleton

A simple class Singleton for create models like 'dynamic settings'

## How to install the package

To install the package, run:

```bash
pip install django-newsingletone
```
In settings.py write next stuff:

```python
INSTALLED_APPS = [
    ...,
    'singleton',
    ...,
]
```

## How to use?

```python
from django.db import models
from singleton.models import Singleton

class DynamicSettings(Singleton):
    setting_name = models.BooleanField(default=False)
    """
    other settings
    ...
    """
```

And then:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Version

Current version: 1.0

## Updates

This package won't have updates, except of bug updates.

## Author

pavelbeard