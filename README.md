# SRVLS

[![Build](https://drone.kputrajaya.com/api/badges/kiloev/srvls/status.svg)](https://drone.kputrajaya.com/kiloev/srvls)

Base for small Django projects running serverless.

Built to shorten setup time, cut down server cost, and enforce good practices.

## Features

#### Develop:
* Debugging

#### Build:
* Code linting
* Unit testing with coverage
* Stack and app deployment
* Domain management

#### Run:
* Serverless database
* Email delivery
* Centralized assets behind CDN
* Centralized logging

## Built With

* [Django](https://www.djangoproject.com/)
* [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
* [Django Nose](https://github.com/django-nose/django-nose)
* [Django Storages](https://github.com/jschneier/django-storages)
* [Coverage](https://github.com/nedbat/coveragepy)
* [Mailgun](https://www.mailgun.com/)
* [S3 SQLite](https://github.com/Miserlou/zappa-django-utils)
* [Watchtower](https://github.com/kislyuk/watchtower)
* [Flake8](http://flake8.pycqa.org/en/latest/)
* [Serverless](https://serverless.com/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [Drone](https://drone.io/)

## How to Use

* Modify `PROJECT_NAME`, `HOST_NAME`, and `AWS_REGION` in `.drone.yml`
* [Sign up](https://cloud.drone.io) for Drone or [setup locally](https://docs.drone.io/installation/github/single-machine/) (tested using `v1.0.0`)
* Enable Drone for your repository
* Add necessary secrets:
    * `AWS_ACCESS_KEY_ID`: Your AWS access key ID (tested using `AdministratorAccess` policy)
    * `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key
    * `MAILGUN_USER`: Your Mailgun SMTP username (optional)
    * `MAILGUN_PASSWORD`: Your Mailgun SMTP password (optional)
    * `CERTIFICATE_ARN`: Your ACM certificate's ARN for `cdn-PROJECT_NAME.HOST_NAME` (must be in `us-east-1`)
* Push to `master` branch to trigger builds
