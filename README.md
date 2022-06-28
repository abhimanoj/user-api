# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK

[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements

- Python 3.6
- Django 3.1
- Django REST Framework

## Installation

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command

```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running

```
pip install -r requirements.txt
```

### Apis

The API you can call from browser based on given url

List-Down all apis and make a post to save data..
http://127.0.0.1:8000/api-

```
http "http://127.0.0.1:8000/api-user-table/"
http "http://127.0.0.1:8000/api-user-details/"
```

GET APIs to fetch students on the basis of course supports filtering

```
http "http://127.0.0.1:8000/api-user-table/?id=<id>"
http "http://127.0.0.1:8000/api-user-details/?email=<emailid>"
```
