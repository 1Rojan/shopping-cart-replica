# Generated by Django 3.1.7 on 2021-03-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0002_auto_20210301_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
