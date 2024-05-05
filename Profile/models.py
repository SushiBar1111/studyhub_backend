from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser

class UserProfile(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    ROLE_CHOICES = (
        ('A Study Mate', 'A Study Mate'),
        ('Someone to Teach', 'Someone to Teach'),
        ('Someone to Learn', 'Someone to Teach'),
    )

    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='A Study Mate')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def ageCalculation(self): #kalkulasi umur berdasarkan birthdate dari pilihan user
        today = date.today()
        user_age = today.year - self.birth_date.year - ((today.month, today.day) < 
        (self.birth_date.month, self.birth_date.day))
        return user_age

    def __str__(self):
        return self.email


