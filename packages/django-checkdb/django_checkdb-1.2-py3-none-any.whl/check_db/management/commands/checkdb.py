import sys
import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

help_string = "Check a database connection."


class Command(BaseCommand):
    help = help_string

    def add_arguments(self, parser):
        parser.add_argument(
            '--database',
            nargs='?',
            type=str,
            help="Name of connection to database, which defined in <your_django_app>/settings.py."
        )
        parser.add_argument(
            '--seconds',
            nargs='?',
            type=int,
            help="Awaiting next attempt to connection. Default - 5 seconds.",
            default=5
        )
        parser.add_argument(
            '--attempts',
            nargs='?',
            type=int,
            help=" Number of attempts. Default - 5.",
            default=5
        )

    def handle(self, *args, **options):
        wait, attempts, database = options['seconds'], options['attempts'], options['database']
        self.stdout.write(f"Wait for connection to the database {database}...")
        conn = None

        att = 0
        for attempt in range(attempts):
            try:
                db_conn = connections[database]
                db_conn.cursor()
                conn = True
                break
            except OperationalError:
                self.stdout.write(f"Connection attempt {database}...")
                time.sleep(wait)
                conn = False
                att += 1

        if conn:
            self.stdout.write(self.style.SUCCESS(f"Successful connection to {database} database!"))
        else:
            self.stdout.write(self.style.ERROR(f"The database {database} hasn't responded after {att} attempts"))
            sys.exit(1)


Command.__doc__ = help_string
