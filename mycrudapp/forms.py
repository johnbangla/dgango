from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        #fields = '__all__'
        fields = ['fullName','emp_Code','mobile_Number','position_Employee']

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position_Employee'].empty_label = "select" 
        self.fields['emp_Code'].required = False   