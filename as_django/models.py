from datetime import datetime
from django.db import models

# Create your models here.
class students(models.Model):
    student_id = models.IntegerField(default=0, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    student_number = models.CharField(max_length=5)
    course = models.CharField(max_length=10)
    def __str__(self):
        return self.first_name

class attendance(models.Model):
    attendance_id = models.IntegerField(default=0, primary_key=True)
    class_date = models.DateTimeField(default=datetime.now, blank=True)
    student1_present = models.CharField(max_length=1)
    student2_present = models.CharField(max_length=1)
    student3_present = models.CharField(max_length=1)
    student4_present = models.CharField(max_length=1)
    student5_present = models.CharField(max_length=1)
    def __str__(self):
        return self.student1_present