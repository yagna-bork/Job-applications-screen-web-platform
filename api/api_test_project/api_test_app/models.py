from django.db import models

# Create your models here.
class Employee(models.Model):
  fName = models.CharField(max_length=20)
  lName = models.CharField(max_length=20)
  emp_id = models.IntegerField()

  def __init__(self, fName, lName):
    self.fName = fName
    self.lName = lName

  def __str__(self):
    return self.fName + " " + self.lName

