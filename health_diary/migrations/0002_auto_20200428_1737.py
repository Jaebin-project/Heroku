# Generated by Django 3.0.5 on 2020-04-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
