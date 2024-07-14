import subprocess
import sys
import os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Remove a cron job'

    def handle(self, *args, **kwargs):
        cron_jobs = settings.CRON_JOBS
        python_path = sys.executable
        manage_py_path = os.path.join(settings.BASE_DIR, 'manage.py')

        for job_name, job_details in cron_jobs.items():
            cron_job = f"{job_details['schedule']} {python_path} {manage_py_path} {job_details['command']}"
            self.remove_cron_job(cron_job)
            self.stdout.write(self.style.SUCCESS(f'Successfully removed cron job: {job_name}'))

    def remove_cron_job(self, cron_job):
        crontab = subprocess.run('crontab -l', shell=True, capture_output=True, text=True).stdout
        new_crontab = "\n".join([line for line in crontab.splitlines() if cron_job not in line])
        subprocess.run(f'echo "{new_crontab}" | crontab -', shell=True, check=True)
