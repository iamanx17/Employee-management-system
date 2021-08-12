from rest_framework import serializers
from core.models import emp_data

class emp_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=emp_data
        fields=['EmpName', 'Age',  'DeptName']