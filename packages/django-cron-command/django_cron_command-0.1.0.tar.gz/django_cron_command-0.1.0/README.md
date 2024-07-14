# DJANGO CRON COMMAND

## Installation
```
pip install django-cron-command
```

## Initialization

1. Add cron_command to your INSTALLED_APPS in settings.py
```
INSTALLED_APPS = [
    ...
    'cron_command',
]
```

2. Create command/task
```
your_app/management/commands/my_custom_command.py
```
```
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Manage cron jobs'

    def add_arguments(self, parser):
        # add sub task

    def handle(self, *args, **options):
        # main task
```

3. Define your cron jobs in settings.py
```
CRON_JOBS = {
    'job1': {
        'schedule': '0 0 * * *',
        'command': 'my_custom_command'
    },
    'job2': {
        'schedule': '*/5 * * * *',
        'command': 'another_custom_command'
    },
    'job3': {
        'schedule': '*/5 * * * *',
        'command': 'another_custom_command run'
    }
}
```

4. Add cron
```
python manage.py cron_add
```

5. Check status
```
python manage.py cron_list
```

6. Remove cron
```
python manage.py cron_remove
```
