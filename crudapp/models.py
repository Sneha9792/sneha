from django.db import models

# Create your models here.

class student(models.Model):
    STUDENT_NO=models.IntegerField(3)
    STUDENT_NAME=models.TextField(max_length=30)
    STUDENT_DOB=models.DateField()
    STUDENT_DOJ=models.DateField()

    def __str__(self):
        return self.title  #this line is used for admin pannel show only title
