from django.urls import path

from . import views


urlpatterns = [
    path('',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('employee/',views.employee, name='employee'),
    path('createEmployee/',views.createEmployee, name='createEmployee'),
    path('jobs/',views.jobs, name='jobs'),
    path('createJobs/',views.createJobs, name='createJobs'),
    path('deductions/',views.deductions, name='deductions'),
    path('createDeductions/',views.createDeductions, name='createDeductions'),
    path('salaryReport/',views.salaryReport, name='salaryReport'),
]