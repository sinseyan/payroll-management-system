from django.db import models
# Create your models here.
class Employee(models.Model):
    empID = models.CharField(max_length=30, primary_key=True, verbose_name="Employee ID")
    lastName = models.CharField(max_length=50, verbose_name="Last Name")
    firstName = models.CharField(max_length=50, verbose_name="First Name")
    middleName = models.CharField(max_length=50,blank=True, verbose_name="Middle Name")
    email = models.EmailField(max_length=50, verbose_name="Email")
    contactNo = models.CharField(max_length=12, verbose_name="Contact Number")
    jobDesc = models.CharField(max_length=30, verbose_name="Job")
    
    def getName(self):
        if self.middleName == " " or "":
            mi = " "
        else:
            mi = self.middleName[0] + ". "

        name = self.lastName + ", " + self.firstName + " " + mi
        return str(name)

    def getSalary(self):
        obj = Jobs.objects.get(jobDesc=self.jobDesc)
        salary = float(obj.salary)

        return float(salary)

    def getPayroll(self):
        deduction = Deductions.objects.all()
        totalDeduct = 0
        for i in deduction:
            totalDeduct += float(i.deduct)

        obj = Jobs.objects.get(jobDesc=self.jobDesc)
        salary = float(obj.salary)
        payroll = salary - totalDeduct
        return float(payroll)

class Jobs(models.Model):
    jobID = models.CharField(max_length=30, primary_key=True,verbose_name="Job ID")
    jobDesc = models.CharField(max_length=50,verbose_name="Job Description")
    salary = models.FloatField(verbose_name="Salary")


class Deductions(models.Model):
    deductID = models.CharField(max_length=30, primary_key=True,verbose_name="Deduction ID")
    deductDesc = models.CharField(max_length=50,verbose_name="Description")
    deduct = models.FloatField(verbose_name="Deduction")