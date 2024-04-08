from django.db import models

class Preference(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    ROLE_CHOICES = (
        ('A Study Mate', 'A Study Mate'),
        ('Someone to Teach', 'Someone to Teach'),
        ('Someone to Learn', 'Someone to Learn'),
    )

    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='A Study Mate')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
