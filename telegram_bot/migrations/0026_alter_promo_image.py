# Generated by Django 3.2.4 on 2021-07-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0025_alter_promo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='image',
            field=models.ImageField(default='uploads/defaults/bot_404.png', upload_to='uploads/promo/%Y_%m_%d', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]