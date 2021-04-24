# Generated by Django 3.1.7 on 2021-04-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_mainuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'super admin'), (2, 'publisher'), (3, 'author')], default=2),
        ),
    ]
