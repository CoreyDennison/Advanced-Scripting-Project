from datetime import datetime
from django.db import models

# Create your models here.
class students(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    student_number = models.CharField(max_length=5)
    course = models.CharField(max_length=10)

class attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    class_date = models.DateTimeField(default=datetime.now, blank=True)
    john_present = models.CharField(max_length=255)
    michael_present = models.CharField(max_length=255)
    beth_present = models.CharField(max_length=255)
    nick_present = models.CharField(max_length=255)
    mark_present = models.CharField(max_length=255)