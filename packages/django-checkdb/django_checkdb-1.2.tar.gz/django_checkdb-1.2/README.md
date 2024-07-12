# django-checkdb

A simple Django package for check connection to your database

## How to install the package

To install the package, run:

```bash
pip install django-checkdb
```
In settings.py write next stuff:

```bash
INSTALLED_APPS = [
    ...other apps...,
    'check_db',
    ...,
]
```

## Check availability

```bash
python manage.py checkdb --database <name>
```

## Version

Current version: 1.1

## Updates

This package won't have updates, except of bug updates.

## Author

pavelbeard