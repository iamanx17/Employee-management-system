from django.contrib import admin
from .models import emp_data, department
# Register your models here.

@admin.register(emp_data)
class emp_dataAdmin(admin.ModelAdmin):
    fields=('EmpName', 'Age', 'DeptName')
    list_display=['EmpId', 'EmpName','Age', 'DeptName']
    list_filter=['DeptName']
    search_fields=['EmpName', 'DeptName']

@admin.register(department)
class depart_admin(admin.ModelAdmin):
    fields=('emp_dpt', 'user')
    list_display=['id','emp_dpt']
    list_filter=['emp_dpt','created_on', 'updated_on']
    search_fields=['emp_dpt']


