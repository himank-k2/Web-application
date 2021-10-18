from django.shortcuts import render, redirect
from App.forms import EmployeeForm,EmployeeForm1
from App.models import Employee
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
import subprocess

def shell(request):
    if request.method == "POST":
        input = request.POST['filename']

        list = subprocess.run(['ls','-la',input],capture_output=True, text=True)
        if list.returncode == 0:
         output = list.stdout.split('\n')
         return render(request,'App/shelloutput.html',{'outputs':output})
        else:
         return HttpResponse("<h1 style ='color:red'>File name does not exists please check the name again</h1>")

    else :
       return render(request,'App/shell.html')

def read(request):
    if request.method == "POST":
        filename = request.POST['filename']
        try:
         file1 = open(filename , 'r')
         Lines = file1.readlines()
         file1.close()
         return render(request, 'App/read.html',{'lines':Lines})
        except:
           return HttpResponse("<h1 style ='color:red'>File not found, Please check the filename or directory</h1>")
    else:
        return render(request,'App/readname.html')

def write(request):
    if request.method == "POST":
        filename= request.POST['filename']
        content =request.POST['content']
        try:
         file1 = open(filename, "a")
         file1.write(content)
         file1.close()
         return HttpResponse("<h1>File written successfully</h1>")
        except:
         return HttpResponse("<h1 style ='color:red'>File not found, Please check the filename or directory</h1>")
    else:
        return render(request,'App/writename.html')


def insert(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('../select/')
            except:
                return HttpResponse(status=404)
        else:
            return HttpResponse(status=404)

    if request.method == "GET":
        form = EmployeeForm()
    return render(request, 'App/index.html', {'form': form},status=200)


def select(request):
    if request.method == "GET":
     employees = Employee.objects.all()
     return render(request, "App/show.html", {'employees': employees},status=200)

def update(request,id):
    if request.method == "POST":
        employee= Employee.objects.get(empId=id)
        form = EmployeeForm1(request.POST,instance=employee)
        if form.is_valid():
           try:
            form.save()
            return redirect('../../select/')
           except:
            return HttpResponse(status=404)
        else:
            return HttpResponse(status=404)

    if request.method == "GET":
        form = EmployeeForm1()
    return render(request,"App/update.html",{'empId':id,'form':form})

def delete(request,id):
    employee= get_object_or_404(Employee,empId=id)
    employee.delete()
    return redirect('../../select/')



