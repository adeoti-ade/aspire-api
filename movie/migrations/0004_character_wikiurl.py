# Generated by Django 3.2.7 on 2021-09-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20210915_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='wikiUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
