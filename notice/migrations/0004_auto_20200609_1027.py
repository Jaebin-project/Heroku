# Generated by Django 2.2.5 on 2020-06-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='board_photos'),
        ),
    ]
