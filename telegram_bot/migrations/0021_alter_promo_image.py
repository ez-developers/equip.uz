# Generated by Django 3.2.4 on 2021-07-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0020_alter_promo_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/promo/%Y_%m_%d', verbose_name='Фото'),
        ),
    ]
