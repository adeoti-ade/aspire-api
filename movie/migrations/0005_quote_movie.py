# Generated by Django 3.2.7 on 2021-09-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_character_wikiurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='movie',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
