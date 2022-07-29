from django.shortcuts import render,redirect
from .forms import Ureg
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/abt.html')

def register(request):
	if request.method == "POST":
		a = Ureg(request.POST)
		if a.is_valid():
			a.save()
			messages.success(request,"User Created Successfuly")
			return redirect('/lgn')
	a = Ureg()
	return render(request,'html/reg.html',{"t":a})