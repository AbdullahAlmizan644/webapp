from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    address=models.TextField()
    birthdate=models.DateField(max_length=100)
    mobile_number=models.BigIntegerField()
    Class=models.CharField(max_length=100)
    roll=models.IntegerField()
    section=models.CharField(max_length=100)
    department=models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} {self.Class}" 



