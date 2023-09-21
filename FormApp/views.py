from django.shortcuts import render,redirect
from FormApp.models import employee
from FormApp.forms import employeeforms
# Create your views here.
# def add(request):
#     form=employeeforms()
#     return render(request,"add_employee.html",{'form':form })
def addemp(request):
    if request.method == 'POST':
        form = employeeforms(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('/show')
    form=employeeforms()
    return render(request,'add_employee.html',{'form':form})

def show(request):
    empls=employee.objects.all()
    return render(request,'show_employee.html',{'empls':empls})

def update(request,id):
    empl=employee.objects.get(id=id)
    form=employeeforms(instance=empl)
    if request.method == 'POST':
        form=employeeforms(request.POST,instance=empl)
        if form.is_valid():
            form.save()
            return redirect('/show')
    return render(request,'update.html',{'form':form})
def delete(request, id):
    emp = employee.objects.get(id=id)
    emp.delete()
    return redirect('/show')
