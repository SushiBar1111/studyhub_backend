# Generated by Django 5.0.6 on 2024-05-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matkul',
            name='matkul',
            field=models.CharField(choices=[('Math', 'Math'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Literature', 'Literature'), ('Coding', 'Coding'), ('Law', 'Law'), ('Accounting', 'Accounting')], max_length=100),
        ),
    ]
