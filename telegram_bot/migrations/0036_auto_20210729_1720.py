# Generated by Django 3.2.4 on 2021-07-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0035_auto_20210729_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_10',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 10'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_5',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 5'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_6',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 6'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_7',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 7'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_8',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 8'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_9',
            field=models.ImageField(null=True, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 9'),
        ),
    ]