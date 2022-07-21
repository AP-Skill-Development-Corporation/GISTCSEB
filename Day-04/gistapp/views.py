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

def edetails(p,empname):
	return HttpResponse("<h3>Hi user <span style='color:red'>{}</span></h3>".format(empname))

def fg(d,j,a):
	return HttpResponse("<html><head><title>Demo</title><style>span{color:red}h3{background-color:green}</style></head><body>Username:  <span>"+j+"</span><h3>"+str(a)+"</h3></body></html>")


def gh(t):
	return render(t,'gt/demo.html')

def ghp(k,n):
	return render(k,'gt/sample.html',{'name':n})

def g(k,deptname,deptno):
	context = {'dname':deptname,'dno':deptno}
	return render(k,'gt/dpt.html',context)

def ph(k,ename,eno,loc):
	context = {'en':ename,'eid':eno,'lo':loc}
	return render(k,'gt/copy.html',context)

def qs(y):
	return HttpResponse("<script>alert('Hi Welcome')</script>")

def qsr(s,ty):
	return HttpResponse("<script>alert('Hi Welcome {}')</script>".format(ty))

def qst(y):
	return HttpResponse("<h3>Hi Welcome <span id='d'></span></h3><script>let z = prompt('Enter Username: '); document.getElementById('d').innerHTML=z;</script>")

def stre(d):
	if d.method == "POST":
		rn = d.POST['r']
		ps = d.POST['p']
		em = d.POST['e']
		yr = d.POST['y']
		return render(d,'gt/sdetails.html',{'roll':rn,'psd':ps,'eml':em,'year':yr})
	return render(d,'std.html')

	