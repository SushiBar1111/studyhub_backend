# Generated by Django 5.0.6 on 2024-05-26 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0012_remove_userprofile_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convo_user1', to='Profile.userprofile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convo_user2', to='Profile.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('Convo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.convo')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.userprofile')),
            ],
        ),
    ]