from django.shortcuts import render
from .serializers import emp_dataSerializer
from rest_framework import viewsets
from core.models import emp_data
from rest_framework.filters import SearchFilter



class EmpApi(viewsets.ModelViewSet):
    queryset=emp_data.objects.all()
    serializer_class=emp_dataSerializer
    fliter_backends=[SearchFilter]
    search_fields=[SearchFilter]
    