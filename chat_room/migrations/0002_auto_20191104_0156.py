# Generated by Django 2.2.6 on 2019-11-03 22:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='invited',
            field=models.ManyToManyField(related_name='invited', to=settings.AUTH_USER_MODEL, verbose_name='Приглашенные участники'),
        ),
    ]
