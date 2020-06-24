# Generated by Django 2.2.5 on 2020-06-23 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0003_auto_20200428_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='img',
            field=models.ImageField(blank=True, upload_to='hospital_images/'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='zone',
            field=models.IntegerField(choices=[(1, '서울'), (2, '경기,인천'), (3, '강원'), (4, '충청'), (5, '전라'), (6, '경상'), (7, '제주')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='Hospital_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='find.Hospital'),
        ),
    ]