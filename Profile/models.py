from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser
from preference.models import Preference
from interest.models import Matkul

class UserProfile(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50, blank=True)
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
    ACADEMIC_LEVEL = (
        ('Senior High School', 'Senior High School'),
        ('Undergraduate', 'Undergraduate'),
        ('Master', 'Master'),
        ('Doctorate', 'Doctorate'),
        ('Employee', 'Employee'),

    )

    STUDY_PLACE = (
        ('Cafe', 'Cafe'),
        ('Library', 'Library'),
        ('Park', 'Park'),
        ('Video Call', 'Video Call'),
        ('Call', 'Call'),

    )

    LEARNING_TYPE = (
        ('Visual Learner', 'Visual Learner'),
        ('Read/Write Learner', 'Read/Write Learner'),
        ('Auditory Learner', 'Auditory Learner'),
        ('Kinsethetic Learner', 'Kinesthetic Learner'),
        ('Solitary Learner', 'Solitary Learner'),
        ('Naturalistic Learner', 'Naturalistic Learner'),
        ('Social Learner', 'Social Learner'),
    )

    MATKUL_CHOICES = (
        ('Math', 'Math'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Literature', 'Literature'),
        ('Coding', 'Coding'), ('Law', 'Law'), ('Accounting', 'Accounting'),
    )

    role = models.CharField(max_length=100, blank=True, null=True, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=6, blank=True, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    academicLevel = models.CharField(max_length=100, blank=True, null=True, choices=ACADEMIC_LEVEL)
    studyPlace = models.CharField(max_length=100, blank=True, null=True, choices=STUDY_PLACE)
    learningType = models.CharField(max_length=100, blank=True, null=True, choices=LEARNING_TYPE)
    matkul = models.CharField(max_length=10, blank=True, null=True, choices=MATKUL_CHOICES)

    def ageCalculation(self): #kalkulasi umur berdasarkan birthdate dari pilihan user
        today = date.today()
        user_age = today.year - self.birth_date.year - ((today.month, today.day) < 
        (self.birth_date.month, self.birth_date.day))
        return user_age
    
    @property
    def age(self):
        return self.ageCalculation() #nyimpen kalkulasi umur user 
    
    def __str__(self):
        return self.email

    def user_profilepicture_path(instance, filename): #path buat nyimpen profile picture
        return f'profile_pictures/user_{instance.id}/{filename}'
    
    profilePicture = models.ImageField(upload_to=user_profilepicture_path, blank=True, null=True) 
    preferences = models.ManyToManyField(Preference, through='filter.UserPreference')
    interest = models.ManyToManyField(Matkul, through='userInterest.UserInterest')


