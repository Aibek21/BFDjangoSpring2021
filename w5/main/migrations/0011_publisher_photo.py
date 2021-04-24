# Generated by Django 3.1.7 on 2021-04-24 06:00

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_author_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pub_photos', validators=[utils.validators.validate_size, utils.validators.validate_extension]),
        ),
    ]