# Generated by Django 3.2.4 on 2021-07-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0017_auto_20210712_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to='uploads/broadcast/%Y_%m_%d', verbose_name='Фото (по желанию)')),
                ('date_published', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название промо-акции')),
                ('image', models.ImageField(upload_to='uploads/promo/%Y_%m_%d', verbose_name='Фото')),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': ('Промоакция',),
                'verbose_name_plural': 'Промокации',
            },
        ),
    ]
