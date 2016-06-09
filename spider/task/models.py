from django.db import models
from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator

# Create your models here.
class StudentForm(models.Model):
    alphaOnly = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed.')
    name = models.CharField(max_length=100,blank=True, null=True, validators=[alphaOnly])
    your_rollno = models.IntegerField(unique=True,validators=[MinValueValidator(100000000),MaxValueValidator(999999999)])
    CHOICES=[('CSE','CSE'),
         ('ECE','ECE'),('EEE','EEE'),('CHEM','CHEM'),('ICE','ICE'),('PROD','PROD'),('META','META')]
    your_dept = models.CharField(max_length=3,choices=CHOICES)
    your_email = models.EmailField()
    your_address = models.CharField(max_length=200,blank=False)
    your_about = models.CharField(max_length=300)

    def __unicode__(self):
    	return self.name

    def __str__(self):
    	return self.name

    




    