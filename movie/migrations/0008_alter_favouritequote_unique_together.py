# Generated by Django 3.2.7 on 2021-09-16 08:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0007_alter_favouritecharacter_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favouritequote',
            unique_together={('user', 'quote')},
        ),
    ]