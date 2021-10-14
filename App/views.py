from django.shortcuts import render, redirect
from App.forms import EmployeeForm,EmployeeForm1
from App.models import Employee


def insert(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../select/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'App/index.html', {'form': form})


def select(request):
    employees = Employee.objects.all()
    return render(request, "App/show.html", {'employees': employees})

def update(request,id):
    if request.method == "POST":
        employee= Employee.objects.get(empId=id)
        form = EmployeeForm1(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('../../select/')

    else:
        form = EmployeeForm1()
    return render(request,"App/update.html",{'empId':id,'form':form})

def delete(request,id):
    employee= Employee.objects.get(empId=id)
    employee.delete()
    return redirect('../../select/')



