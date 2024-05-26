from django.db import models

class Matkul(models.Model):
    MATKUL_CHOICES = (
        ('Math', 'Math'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Literature', 'Literature'),
        ('Coding', 'Coding'), ('Law', 'Law'), ('Accounting', 'Accounting'),
    )
    matkul = models.CharField(max_length=10, choices=MATKUL_CHOICES)
    
    def __str__(self):
        return self.matkul