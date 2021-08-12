from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class department(models.Model):
    id=models.AutoField(primary_key=True)
    emp_dpt=models.CharField(max_length=300, help_text='Enter the department of the employee', unique=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on=models.DateTimeField(auto_now=False, auto_now_add=True)
    created_on=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.emp_dpt
    

class emp_data(models.Model):
    EmpId=models.AutoField(primary_key=True)
    EmpName=models.CharField(max_length=250, help_text='Enter the name of the employee')
    Age=models.IntegerField(help_text='Enter the age of the employee')
    DeptName=models.ForeignKey(department, on_delete=models.CASCADE)

    class Meta:
        ordering=['EmpId']
    
    def __str__(self):
        return self.EmpName  +" "+  str(self.DeptName)