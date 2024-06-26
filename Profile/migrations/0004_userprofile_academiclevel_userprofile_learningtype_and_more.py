# Generated by Django 5.0.6 on 2024-05-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_userprofile_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='academicLevel',
            field=models.CharField(blank=True, choices=[('Senior High School', 'Senior High School'), ('Undergraduate', 'Undergraduate'), ('Master', 'Master'), ('Doctorate', 'Doctorate'), ('Employee', 'Employee')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='learningType',
            field=models.CharField(blank=True, choices=[('Visual Learner', 'Visual Learner'), ('Read/Write Learner', 'Read/Write Learner'), ('Auditory Learner', 'Auditory Learner'), ('Kinsethetic Learner', 'Kinesthetic Learner'), ('Solitary Learner', 'Solitary Learner'), ('Naturalistic Learner', 'Naturalistic Learner'), ('Social Learner', 'Social Learner')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='studyPlace',
            field=models.CharField(blank=True, choices=[('Cafe', 'Cafe'), ('Library', 'Library'), ('Park', 'Park'), ('Video Call', 'Video Call'), ('Call', 'Call')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, choices=[('A Study Mate', 'A Study Mate'), ('Someone to Teach', 'Someone to Teach'), ('Someone to Learn', 'Someone to Teach')], default='A Study Mate', max_length=100, null=True),
        ),
    ]
