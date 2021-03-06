# Generated by Django 3.1.7 on 2021-03-06 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('website', models.CharField(blank=True, max_length=100, null=True, verbose_name='Веб сайт')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('num_pages', models.IntegerField(default=0, verbose_name='Количество страниц')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='books', to='main.author', verbose_name='Автор')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='books', to='main.publisher', verbose_name='Издатель')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-publication_date'],
            },
        ),
    ]
