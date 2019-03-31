# SRVLS

[![Build](https://drone.kputrajaya.com/api/badges/kiloev/srvls/status.svg)](https://drone.kputrajaya.com/kiloev/srvls)

Base for small Django projects running serverless.

Built to shorten setup time, cut down server cost, and enforce good practices.

#### Develop:
* Debugging

#### Build:
* Code linting
* Unit testing
* Stack and app deployment
* Domain management

#### Run:
* Serverless database
* Email delivery
* Centralized assets behind CDN
* Centralized logging

## Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
* [Django Storages](https://github.com/jschneier/django-storages)
* [Mailgun](https://www.mailgun.com/)
* [S3 SQLite](https://github.com/Miserlou/zappa-django-utils)
* [Watchtower](https://github.com/kislyuk/watchtower)
* [Flake8](http://flake8.pycqa.org/en/latest/)
* [Serverless](https://serverless.com/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [Drone](https://drone.io/)

## How to Use

* Configure `PROJECT_NAME` and `HOST_NAME` in `.drone.yml`
* Setup Drone (currently v1.0.0) for your repository
* Add necessary secrets:
    * `AWS_ACCESS_KEY_ID`
    * `AWS_SECRET_ACCESS_KEY`
    * `MAILGUN_USER`
    * `MAILGUN_PASSWORD`
    * `CERTIFICATE_ARN`
