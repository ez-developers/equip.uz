# Generated by Django 3.2.4 on 2021-07-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0032_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='text',
            field=models.TextField(max_length=1024, null=True, verbose_name='Текст'),
        ),
    ]
