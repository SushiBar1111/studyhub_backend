# Generated by Django 5.0.6 on 2024-06-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preference', '0008_alter_preference_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True),
        ),
    ]