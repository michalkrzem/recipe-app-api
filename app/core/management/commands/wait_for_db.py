"""
Django commant to wait for database to be avaliable
"""
from django.core.management.base import BaseCommand

import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **kwargs):
        """Entrypoint for command"""
        self.stdout.write("Waiting for database to be avaliable")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
