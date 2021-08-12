from django.shortcuts import render, redirect
from .models import emp_data,department
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

#Home page
def home(request):
    emp=emp_data.objects.all()
    dpt=department.objects.all()
    emplist=[]
    dptlist=[]
    for i in emp:
        emplist.append(i)
    for i in dpt:
        dptlist.append(i)
    return render(request,'core/index.html', {'emp':len(emplist), 'dpt':len(dptlist)})

#department page
def dpt_sec(request):
    dpt=department.objects.all()
    return render(request, 'emp/dpt_sec.html',{'dpt':dpt})

#Add Employee page
def emp_sec(request):
    dpt=department.objects.all()
    return render(request, 'emp/emp_sec.html',{'dpt':dpt})
#Employee list page
def emp(request):
    employee=emp_data.objects.all()
    dpt=department.objects.all()
    return render(request, 'emp/Emp.html',{'employee':employee,'dpt':dpt})


#function of department
def add_dpt(request):
    if request.method=='POST':
        user=request.user
        dpt=request.POST.get('dpt_name')
        if not department.objects.filter(emp_dpt=dpt).exists():
            dpart=department(emp_dpt=dpt, user=user)
            dpart.save()
            return redirect('/dpt_sec/')
        else:
            messages.warning(request, 'Department already exists')
            return redirect('/dpt_sec/')
    return render(request, 'emp/dpt_sec.html')

def dlt_dpt(request):
    if request.method=='POST':
        dpt=request.POST.get('dpt')
        depart=department.objects.filter(emp_dpt=dpt)
        depart.delete()
        return redirect('/dpt_sec/')
    return render(request, 'emp/dpt_sec.html')

def update_dpt(request):
    if request.method=='POST':
        id=request.POST.get('id')
        dpt_name=request.POST.get('dpt_name')
        depart=department.objects.get(id=id)
        depart.emp_dpt=dpt_name
        depart.save()
        return redirect('/dpt_sec/')

def edit_dpt(request, id):
    dpt=department.objects.get(id=id)
    return render(request, 'emp/up_dpt.html',{'dpt':dpt})

def add_emp(request):
    if request.method=='POST':
        emp_name=request.POST.get('emp_name')
        age=request.POST.get('age')
        id=request.POST.get('id')
        dpt=department.objects.get(id=id)
        emp=emp_data(EmpName=emp_name, Age=age, DeptName=dpt)
        emp.save()
        return redirect('/emp_sec/')
    return render(request, 'emp/emp_sec.html')

def edit_emp(request, id):
    emp=emp_data.objects.get(EmpId=id)
    dpt=department.objects.all()
    return render(request, 'emp/up_emp.html',{'emp':emp, 'dpt':dpt})

def update_emp(request):
    if request.method=='POST':
        id=request.POST.get('id')
        empname=request.POST.get('empname')
        age=request.POST.get('age')
        dpt=request.POST.get('dpt')          
        emp=emp_data.objects.get(EmpId=id)
        depart=department.objects.get(id=dpt)  

        emp.EmpName=empname
        emp.Age=age
        emp.DeptName=depart
        emp.save()      
        return redirect('/emp/')


def dlt_emp(request):
    if request.method=='POST':
        id=request.POST.get('emp_id')
        emp=emp_data.objects.get(EmpId=id)
        emp.delete()
        return redirect('/emp/')
    return render(request, 'emp/Emp.html')



#Function for user account work login, logout, register
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        firstname=request.POST['first_name']
        lastname=request.POST['lastname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username has already taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email has already taken')
                return redirect('/register/')
            else:
                user=User.objects.create_user(firstname=firstname, lastname=lastname, username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'your account has been created successfully')
                messages.success(request, 'Please wait for the admin to confirm your account')
                return redirect('/')
        else:
            messages.warning(request, 'Password not matched')
            return redirect('/register/')
    return render(request,'account/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user!=None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'username not found')
            return redirect('/login/')
    return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')