# Generated by Django 3.2.4 on 2021-07-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0034_auto_20210726_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_10',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_5',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_6',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_7',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_8',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 8'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_9',
            field=models.ImageField(default=None, upload_to='uploads/products/%Y_%m_%d/', verbose_name='Фото 9'),
            preserve_default=False,
        ),
    ]
