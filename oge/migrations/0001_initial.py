# Generated by Django 4.0.5 on 2022-06-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockAlgebraOge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_algebra_oge', models.CharField(max_length=255, verbose_name='Название блока')),
                ('file_algebra_oge', models.FileField(upload_to='algebra/', verbose_name='Файл блока')),
            ],
            options={
                'verbose_name': 'Программа блока Алгебра ОГЭ',
                'verbose_name_plural': 'Программы блоков Алгебра ОГЭ',
            },
        ),
        migrations.CreateModel(
            name='BlockGeometriaOge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_geometria_oge', models.CharField(max_length=255, verbose_name='Название блока')),
                ('file_geometria_oge', models.FileField(upload_to='geometria/', verbose_name='Файл блока')),
            ],
            options={
                'verbose_name': 'Программа блока Геометрия ОГЭ',
                'verbose_name_plural': 'Программы блоков Геометрия ОГЭ',
            },
        ),
        migrations.CreateModel(
            name='VariantOge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_oge', models.CharField(max_length=255, verbose_name='Номер варианта')),
                ('file_oge', models.FileField(upload_to='ege/', verbose_name='Файл варианта')),
            ],
            options={
                'verbose_name': 'Вариант ОГЭ',
                'verbose_name_plural': 'Варианты ОГЭ',
            },
        ),
    ]
