# Generated by Django 4.0.5 on 2022-06-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_cert', models.CharField(max_length=255, verbose_name='Название сертификата')),
                ('file_cert', models.FileField(upload_to='cert/', verbose_name='Файл сертификата')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
    ]
