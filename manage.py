#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'srvls.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    testing = len(sys.argv) > 1 and sys.argv[1] == 'test'
    if testing:
        import coverage
        cov = coverage.coverage()
        cov.erase()
        cov.start()

    execute_from_command_line(sys.argv)

    if testing:
        cov.stop()
        cov.save()
        cov.report()
