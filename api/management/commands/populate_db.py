from django.core.management.base import BaseCommand
from api.models import User, Contact, Spam
from django.contrib.auth.hashers import make_password
import faker
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = faker.Faker()
        
        # Create sample users
        for _ in range(10):
            username = fake.user_name()
            phone_number = fake.phone_number()[:20]  # Truncate to ensure it's within the limit
            email = fake.email()
            User.objects.create(
                username=username,
                phone_number=phone_number,
                email=email,
                password=make_password('password123')
            )

        # Create sample contacts
        users = User.objects.all()
        for user in users:
            for _ in range(5):
                Contact.objects.create(
                    user=user,
                    name=fake.name(),
                    phone_number=fake.phone_number()[:20],  # Truncate to ensure it's within the limit
                    email=fake.email()
                )

        # Create sample spam entries
        for _ in range(10):
            Spam.objects.create(
                phone_number=fake.phone_number()[:20],  # Truncate to ensure it's within the limit
                spam_likelihood=random.uniform(0, 1)
            )
