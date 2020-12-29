# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from model_utils import Choices

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey('Course', on_delete=models.CASCADE,
                               null=True) 
    roles = Choices('Student', 'Teacher')
    role = models.CharField(max_length=50, choices=roles) 
    
    def __str__(self):
        return self.username


class Course(models.Model):
    all_courses = [
    ('Engineering', (
            ('Software Engineering', 'SE'),
            ('Computer Engineering', 'CE'),
            ('Electrical Engineering', 'EE'),
        )
    ),
    ('Commerce', (
            ('Bachelor of Business Administration', 'BBA'),
            ('Chartered Accountancy', 'CA'),
        )
    ),
    ('Medical', (
            ('Neuroscience', 'NS'),
            ('Bachelor of Medicine, Bachelor of Surgery', 'MBBS'),
        )
    ),
    ]
    courses = models.CharField(max_length=100, choices=all_courses,
                                unique=True)


    def __str__(self):
        return self.courses



