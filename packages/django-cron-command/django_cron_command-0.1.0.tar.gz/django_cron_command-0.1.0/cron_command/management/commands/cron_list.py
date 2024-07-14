import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand
import sys
import os

class Command(BaseCommand):
    help = 'List all cron jobs'

    def handle(self, *args, **kwargs):
        self.list_cron_jobs()

    def list_cron_jobs(self):
        # Fetch the crontab entries
        crontab = subprocess.run('crontab -l', shell=True, capture_output=True, text=True).stdout
        crontab_lines = crontab.splitlines()

        cron_jobs = settings.CRON_JOBS
        found_jobs = set()

        # Print header
        self.stdout.write(self.style.SUCCESS('Current cron jobs:'))

        # Match crontab lines with CRON_JOBS entries
        for line in crontab_lines:
            for job_name, job_details in cron_jobs.items():
                cron_schedule = job_details['schedule']
                cron_command = job_details['command']
                python_path = sys.executable
                manage_py_path = os.path.join(settings.BASE_DIR, 'manage.py')
                cron_job = f"{job_details['schedule']} {python_path} {manage_py_path} {job_details['command']}"

                if cron_job == line:
                    found_jobs.add(job_name)
                    self.stdout.write(self.style.SUCCESS(f"\nJob Name: {job_name}"))
                    self.stdout.write(f"Schedule: {cron_schedule}")
                    self.stdout.write(f"Command: {cron_command}")
                    self.stdout.write('-' * 40)
                    break

        # Identify jobs from CRON_JOBS not found in crontab
        for job_name, job_details in cron_jobs.items():
            if job_name not in found_jobs:
                self.stdout.write(self.style.WARNING(f"\nJob Name: {job_name} is not found in crontab"))

        # List other cron jobs not defined in the CRON_JOBS setting
        other_jobs = [
            line for line in crontab_lines
            if not any(
                line.startswith(job_details['schedule']) and job_details['command'] in line
                for job_details in cron_jobs.values()
            )
        ]
        
        if other_jobs:
            self.stdout.write(self.style.WARNING('\nOther cron jobs:'))
            for line in other_jobs:
                self.stdout.write(line)
