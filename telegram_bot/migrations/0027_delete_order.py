# Generated by Django 3.2.4 on 2021-07-18 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0026_alter_promo_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
