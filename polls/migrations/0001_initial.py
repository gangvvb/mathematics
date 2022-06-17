# Generated by Django 4.0.5 on 2022-06-17 13:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Название теста')),
                ('worktime', models.IntegerField(verbose_name='Время выполнения (мин)')),
                ('questionscount', models.IntegerField(verbose_name='Количество вопросов')),
                ('statisfactorily', models.IntegerField(verbose_name='Удовлетворительно')),
                ('good', models.IntegerField(verbose_name='Хорошо')),
                ('perfect', models.IntegerField(verbose_name='Отлично')),
            ],
            options={
                'verbose_name': 'Тесты',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, verbose_name='ФИО')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время завершения')),
                ('rating', models.FloatField(verbose_name='Проценты')),
                ('profileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.profile', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('profileid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.profile', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('isright', models.BooleanField()),
                ('questionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответа',
            },
        ),
    ]
