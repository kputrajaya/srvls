# Srvls

[![Build](https://drone.kputrajaya.com/api/badges/kiloev/srvls/status.svg)](https://drone.kputrajaya.com/kiloev/srvls)

Base for Django projects running in serverless environment.

## Built with

* [Django](https://www.djangoproject.com/)
* [Serverless](https://serverless.com/)
* [Serverless API Gateway Binary](https://github.com/maciejtreder/serverless-apigw-binary)
* [Serverless Domain Manager](https://github.com/amplify-education/serverless-domain-manager)
* [Serverless Python Requirements](https://github.com/UnitedIncome/serverless-python-requirements)
* [Serverless WSGI](https://github.com/logandk/serverless-wsgi)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [Python 3.7](https://www.python.org/)
* [Drone](https://drone.io/)

## Project Setup

* [Flake8](http://flake8.pycqa.org/en/latest/): Code linting
* [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar): On-view debugging
* [Django Storages](https://github.com/jschneier/django-storages): Assets on S3
* [Mailgun](https://www.mailgun.com/): Sending real emails
* [Watchtower](https://github.com/kislyuk/watchtower): Logging to CloudWatch

## How to Use

* Configure `PROJECT_NAME` and `HOST_NAME` in `.drone.yml`.
* Setup Drone (currently using v1.0.0) for your repository.
* Add necessary secrets:
    * `AWS_ACCESS_KEY_ID`
    * `AWS_SECRET_ACCESS_KEY`
    * `MAILGUN_USER`
    * `MAILGUN_PASSWORD`
    * `CERTIFICATE_ARN`
