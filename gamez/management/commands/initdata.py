from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import User
from gamez.models import Collection
import hashlib


class Command(BaseCommand):
    help = "DEV COMMAND: Fill database with a set of data for testing purposes"

    def handle(self, *args, **options):

        call_command('loaddata', 'users')
        call_command('loaddata', 'platforms')
        call_command('loaddata', 'collections')
        call_command('loaddata', 'games')

        # Convert the plain text passwords to secure hashes
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()

        # Convert the sharing keys to secure hashes
        for collection in Collection.objects.all():
            collection.key = hashlib.sha256(collection.key.encode('utf-8')).hexdigest()
            collection.save()