# Generated by Django 2.2 on 2021-10-22 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0004_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stream_following', to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
