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

    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='A Study Mate')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
    academicLevel = models.CharField(max_length=100, blank=True, null=True, choices=ACADEMIC_LEVEL)
    studyPlace = models.CharField(max_length=100, blank=True, null=True, choices=STUDY_PLACE)
    learningType = models.CharField(max_length=100, blank=True, null=True, choices=LEARNING_TYPE)