# SRVLS

[![Build](https://drone.kputrajaya.com/api/badges/kiloev/srvls/status.svg)](https://drone.kputrajaya.com/kiloev/srvls)

Base for small Django projects running in serverless environment.

Built to shorten setup time, cut down server cost, and enforce good practices.

### Develop:
* Debugging

### Build:
* Code linting
* Unit testing
* Stack and app deployment
* Domain management

### Run:
* Serverless database
* Email delivery
* Centralized assets behind CDN
* Centralized logging

## Built with

* [Django](https://www.djangoproject.com/)
* [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
* [Django Storages](https://github.com/jschneier/django-storages)
* [Flake8](http://flake8.pycqa.org/en/latest/)
* [Mailgun](https://www.mailgun.com/)
* [S3-SQLite](https://github.com/Miserlou/zappa-django-utils)
* [Watchtower](https://github.com/kislyuk/watchtower)
* [Serverless](https://serverless.com/)
* [Serverless APIGW Binary](https://github.com/maciejtreder/serverless-apigw-binary)
* [Serverless Domain Manager](https://github.com/amplify-education/serverless-domain-manager)
* [Serverless Python Requirements](https://github.com/UnitedIncome/serverless-python-requirements)
* [Serverless WSGI](https://github.com/logandk/serverless-wsgi)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [Python 3.7](https://www.python.org/)
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
* Profit
