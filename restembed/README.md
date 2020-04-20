# Django Frontend GUI

A light-weighted GUI which talks to external API for data. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Postgres: brew install postgres
Python3
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
pip3 install requirements.txt (you may comment out the heroku part for local run)
login to local postgres and do: create database django_gui
run db migration under project directory: python manage.py migrate
create 1 set of admin users(lonk.admin, lonk.user1, lonk.user2 etc): python manage.py createsuperuser
commented out last 2 lines for heroku part in restembed/settings.py
run server: python manage.py runserver
```

## Key Features
### Encrypted external API call
Outgoing calls from this app has its credential encrypted with AES algorithm
https://github.com/deoshao11/django-gui/blob/master/restembed/core/views.py#L97

### JQuery UI components
This app extensively uses JQuery Datatable and JsTree to render data received from API calls.

### Persistence Layer
Every external call response is saved in postgres for data persistence and audit purpose.

## Deployment

git push remote would automatically trigger the heroku build and deploy.

## Migration
Heroku: Fork or bring this repo private and then create a new heroku app with below instrution:
https://devcenter.heroku.com/categories/working-with-django

AWS: AWS BeanStalk could be an ideal place for hosting Django App:
https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/
