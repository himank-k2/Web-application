from django.db import models

class Employee(models.Model):
    empId = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary =models.IntegerField()
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.name

# Create your models here.
