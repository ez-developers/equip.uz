# Generated by Django 3.2.4 on 2021-07-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0013_auto_20210710_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notifications',
            field=models.BooleanField(default=True),
        ),
    ]
