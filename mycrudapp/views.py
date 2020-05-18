from .models import Employee
from django.shortcuts import render,redirect
from .forms import EmployeeForm

#Line Total: 03 function Name:  emp_list responsible: show all recodrds html file name: pageshow.html
def emp_list(request):
    context = Employee.objects.all()
    return render(request,'pageshow.html',{'emp_list' : context})

#Line Total: 02 function Name:  emp_home responsible: show home page  html file name: home.html
def emp_home(request):
     return render(request,'home.html')

#Line Total: 17 function Name:  emp_form responsible: insert,edit, update 
def emp_form(request,id=0):
    if request.method == "GET":
        if id == 0:   #if first request the show only insert form
            form = EmployeeForm()
        else:#if old request the show only insert form with records and edit performs
            employee = Employee.objects.get(pk=id) 
            form = EmployeeForm(instance = employee)   
        context = {'form' : form}
        return render(request,'pageinsert.html',context)
    else:#if post  request the show only insert form
         if id == 0: #if first request the show only insert form
            form = EmployeeForm(request.POST)
         else: #if old request the show only insert form with update option
            employee = Employee.objects.get(pk=id) 
            form = EmployeeForm(request.POST,instance = employee)
         if form.is_valid():
            form.save()    
         return redirect('/list')#if request is done go to show record page

#Line Total: 03 function Name:  emp_delete responsible: delete
def emp_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')    

def emp_details(request,id):
    employee = Employee.objects.get(pk=id)
    context = {'employee' : employee}
    return render(request,'pagedetails.html',context)        


