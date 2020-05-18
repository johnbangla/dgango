from django.db import models

class Position(models.Model):

    title = models.CharField(max_length=20)

    

    def __str__(self):
        return self.title

    

# Create your models here.
class Employee (models.Model):

    fullName = models.CharField(max_length=50)
    emp_Code = models.CharField(max_length=20)
    mobile_Number = models.CharField(max_length=20)
    position_Employee = models.ForeignKey(Position,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.fullName

 
