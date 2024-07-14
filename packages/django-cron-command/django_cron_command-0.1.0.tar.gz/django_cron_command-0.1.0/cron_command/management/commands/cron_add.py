import subprocess
import sys
import os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Add a cron job'

    def handle(self, *args, **kwargs):
        cron_jobs = settings.CRON_JOBS
        python_path = sys.executable
        manage_py_path = os.path.join(settings.BASE_DIR, 'manage.py')

        for job_name, job_details in cron_jobs.items():
            cron_job = f"{job_details['schedule']} {python_path} {manage_py_path} {job_details['command']}"
            if not self.cron_job_exists(cron_job):
                self.add_cron_job(cron_job)
                self.stdout.write(self.style.SUCCESS(f'Successfully added cron job: {job_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Cron job already exists: {job_name}'))

    def cron_job_exists(self, cron_job):
        result = subprocess.run('crontab -l', shell=True, capture_output=True, text=True)
        return cron_job in result.stdout

    def add_cron_job(self, cron_job):
        cron_line = f'(crontab -l; echo "{cron_job}") | crontab -'
        subprocess.run(cron_line, shell=True, check=True)
