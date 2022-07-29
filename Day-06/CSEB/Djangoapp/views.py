from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.

def home(request):
	return render(request,'html/hm.html')

def cd(request):
	p = Employee.objects.all()
	if request.method=="POST":
		empid = request.POST['ed']
		empname = request.POST['en']
		empage = request.POST['ea']
		empexp = request.POST['exp']
		s = Employee(eid=empid,ename=empname,eage=empage,eexp=empexp)
		s.save()
		return redirect('/')
	return render(request,'html/crud.html',{'fr':p})


def emup(request,h):
	b = Employee.objects.get(eid=h)
	if request.method == "POST":
		b.eid = request.POST['ed']
		b.ename = request.POST['en']
		b.eage = request.POST['ea']
		b.save()
		return redirect('/')
	return render(request,'html/eupd.html',{'c':b})

def emdt(request,k):
	b = Employee.objects.get(eid=k)
	if request.method == "POST":
		b.delete()
		return redirect('/')
	return render(request,'html/edt.html',{'c':b})