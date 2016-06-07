from django.db import models

# Create your models here.
class StudentForm(models.Model):
    your_name = models.CharField(max_length=100)
    your_rollno = models.IntegerField()
    CHOICES=[('CSE','CSE'),
         ('ECE','ECE'),('EEE','EEE'),('CHEM','CHEM'),('ICE','ICE'),('PROD','PROD'),('META','META')]
    your_dept = models.CharField(max_length=3,choices=CHOICES)
    your_email = models.EmailField(max_length=100)
    your_address = models.CharField(max_length=200)
    your_about = models.CharField(max_length=300)