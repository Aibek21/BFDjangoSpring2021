# Generated by Django 3.1.7 on 2021-04-03 05:00

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210327_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[main.models.num_pages_range_validation], verbose_name='Количество страниц'),
        ),
    ]
