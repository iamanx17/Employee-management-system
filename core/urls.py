from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='Home'),

    #Employee, department , full employee
    path('emp_sec/', views.emp_sec, name='Employee section'),
    path('dpt_sec/', views.dpt_sec, name='department section'),
    path('emp/', views.emp, name='employee'),
    
    #department section
    path('add_dpt/', views.add_dpt, name='Add department'),
    path('dlt_dpt/', views.dlt_dpt, name='delete department'),
    path('update_dpt/', views.update_dpt, name='edit department'),
    path('edit_dpt/<int:id>', views.edit_dpt, name='edit department'),
    
    #employee section
    path('add_emp/', views.add_emp, name='Add employee'),
    path('dlt_emp/', views.dlt_emp, name='delte employee'),
    path('update_emp/', views.update_emp, name='edit employee'),
    path('edit_emp/<int:id>', views.edit_emp, name='edit employee'),


    #api
    path('api/', include('core.serializers.urls')),
    
    #account paths
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]