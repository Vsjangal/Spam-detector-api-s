# Generated by Django 5.1 on 2024-08-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=1234567890, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]