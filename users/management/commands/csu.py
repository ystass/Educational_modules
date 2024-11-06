from django.core.management import BaseCommand

from users.models import User
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(email=os.getenv("ADMIN_USER"),)
        user.set_password(os.getenv("ADMIN_PASSWORD"))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
