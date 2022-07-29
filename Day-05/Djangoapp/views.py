from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'html/hm.html')

def cd(request):
	return render(request,'html/crud.html')