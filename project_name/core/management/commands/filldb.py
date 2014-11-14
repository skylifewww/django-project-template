import sys

from django.core.management import call_command
from django.core.management.base import BaseCommand

from {{ project_name }}.users.factories import generate_users


class Command(BaseCommand):
    help = 'Fill the database with test fixtures'

    def handle(self, *args, **options):
        sys.stdout.write('Starting fill db\r\n')

        fixture_list = ['config']
        call_command('loaddata', *fixture_list)

        generate_users()

        sys.stdout.write('Completed fill db\r\n')
