# Generated by Django 5.0.3 on 2024-04-07 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0004_alter_userprofile_role'),
        ('preference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preference.preference')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.userprofile')),
            ],
        ),
    ]
