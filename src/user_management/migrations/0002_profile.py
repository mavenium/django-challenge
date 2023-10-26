# Generated by Django 4.2.6 on 2023-10-26 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile_user', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Last Name')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(None, '---------'), (0, 'Male'), (1, 'Female')], verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'user_management_profiles',
                'ordering': ['user_id'],
            },
        ),
    ]
