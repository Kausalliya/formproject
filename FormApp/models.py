from django.db import models

# Create your models here.
class employee(models.Model):
    empid = models.IntegerField()
    emp_name = models.CharField(max_length=25)
    emp_address = models.CharField(max_length=25)
