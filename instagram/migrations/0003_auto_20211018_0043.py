# Generated by Django 2.2 on 2021-10-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20211017_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to='Profile/'),
        ),
    ]
