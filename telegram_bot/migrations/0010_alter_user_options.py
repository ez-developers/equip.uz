# Generated by Django 3.2.4 on 2021-07-10 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0009_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True, 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
