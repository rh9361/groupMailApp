from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=162)

    def __str__(self):
        return self.name

class Group(models.Model):
    email = models.ForeignKey(Student,on_delete=True)
    groupName = models.CharField(max_length=50)

    def __str__(self):
        return self.groupName
