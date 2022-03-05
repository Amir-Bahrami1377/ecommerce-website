from argparse import ArgumentParser
from account.models import Customer
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'A django command for activate and deactivate users!'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-i', '--id', help='Enter user id please')

    def handle(self, *args, **options):
        user_id = options['id']
        user = Customer.objects.get(user_ptr_id=user_id)
        if user:
            user_status = user.is_active
            if user_status:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        else:
            raise CommandError("invalid user id!")

        print(self.style.SUCCESS('done'))
