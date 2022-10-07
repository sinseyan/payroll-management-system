from django import forms
from .models import Employee, Jobs, Deductions


# creating a form


class EmployeesForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = [
            "empID",
            "lastName",
            "firstName",
            "middleName",
            "email",
            "contactNo",
            "jobDesc"
        ]
    jobDesc = forms.ModelChoiceField(label="Job",queryset=Jobs.objects.all().values_list('jobDesc',flat=True),to_field_name="jobDesc")
    

class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = [
            "jobID",
            "jobDesc",
            "salary",
        ]

class DeductionsForm(forms.ModelForm):
    class Meta:
        model = Deductions
        fields = [
            "deductID",
            "deductDesc",
            "deduct",
        ]
