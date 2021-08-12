from django import forms
from .models import emp_data,department
from django.contrib.auth.models import User

class emdata_form(forms.ModelForm):
    class Meta:
        model=emp_data
        fields='__all__'


class dpt_form(forms.ModelForm):
    class Meta:
        model=department
        fields='__all__'
    
class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields='firstname, lastname, email, username, password'

