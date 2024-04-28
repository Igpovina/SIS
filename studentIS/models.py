from django.db import models
from django.contrib.auth.models import AbstractUser, User, Permission

# Create your models here.
class Classes(models.Model):
    subject = models.CharField(max_length=30, blank=True, null=True)
    schedule_start = models.DateTimeField()
    schedule_end = models.DateTimeField()
    class_duration = models.CharField(max_length=25, default="90 minutes")

class Course(models.Model):
    classes = models.ManyToManyField(Classes)


class User(AbstractUser):
    is_student = models.BooleanField('is_student', default=False)
    is_faculty = models.BooleanField('is_faculty', default=False)
    def student(self):
        if self.is_student:
            student_classes = models.ManyToManyField(Course, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=False, default='None')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(null=True, blank=True, upload_to = 'media/', default='default_profile_picture.jpg')

# class Teacher(User):
#     sex = models.CharField(max_length=20, blank=False, null=False)
    