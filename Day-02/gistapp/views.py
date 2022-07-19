from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(request):
	return HttpResponse("Welcome to Django Workshop")

def demo1(request,cge):
	return HttpResponse("hello {}".format(cge))

def trail(request,en,ea):
	return HttpResponse("Employee Name is: {}\nEmployee Age is: {}".format(en,ea))
def student(request,name,dept,sno,marks):
	return HttpResponse("Name is: {}\ndept name is: {}\nroll number is: {}\n marks are: {}".format(name,dept,sno,marks))

def ran(p,r):
	return HttpResponse("<h3>Random Number is: {}</h3>".format(r))

