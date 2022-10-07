from django.shortcuts import render,redirect
from .models import Employee, Jobs, Deductions
from .forms import EmployeesForm, JobsForm, DeductionsForm

# Create your views here.
def login(request):
    if request.method == "POST":
        user = request.POST['login']
        password = request.POST['password']

        if user == "admin" and password == "password":
            return redirect("/payroll/home")

    return render(request,'payroll/login.html')

def home(request):
    countJobs = Jobs.objects.all().count()
    countEmp = Employee.objects.all().count()
    data = Employee.objects.all()
    context = {
        "countJobs" : int(countJobs),
        "countEmp" : int(countEmp),
        "data" : data,
    }

    return render(request,'payroll/home.html',context)

def createEmployee(request): 
    form = EmployeesForm(request.POST or None)

    if form.is_valid():
        
        form.save()
        form.cleaned_data['jobDesc'].save()
        
        return redirect('employee')   

    return render(request,'payroll/createEmployee.html',{'form':form})    

def employee(request):
    data = Employee.objects.all()
    context = {
        "data" : data,
    }
    return render(request,'payroll/employee.html',context)


def jobs(request):
    obj = Jobs.objects.all()
    context = {
        "data" : obj,
    }
    return render(request,'payroll/jobs.html',context)

def createJobs(request): 
    form = JobsForm(request.POST or None)
    if form.is_valid():
        
        form.save()

        
        return redirect('jobs')   

    return render(request,'payroll/createJobs.html',{'form':form}) 

def deductions(request):
    obj = Deductions.objects.all()
    total = 0
    for i in obj:
        total += float(i.deduct)

    context = {
        "data" : obj,
        "total" : total,
    }
    
    return render(request,'payroll/deductions.html',context)

def createDeductions(request): 
    form = DeductionsForm(request.POST or None)
    if form.is_valid():
        
        form.save()

        
        return redirect('deductions')   

    return render(request,'payroll/createDeductions.html',{'form':form}) 


def salaryReport(request): 
    
    emp = Employee.objects.all()

    deduction = Deductions.objects.all()
    totalDeduct = 0
    for i in deduction:
        totalDeduct += float(i.deduct)



    context={
        "data" : emp,
        "totalDeduction" : totalDeduct,
    }

    


    return render(request,'payroll/salaryReport.html',context) 

    
