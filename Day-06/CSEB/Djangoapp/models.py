from django.db import models

# Create your models here.

class Employee(models.Model):
	r = [
		('0','Select Experience Year'),
		('1','Year'),
		('2','2 Years'),
		('3','3 Years'),
	]
	eid = models.CharField(max_length=50)
	ename = models.CharField(max_length=150)
	eage = models.IntegerField(default=20)
	eexp = models.CharField(max_length=10,choices=r,default='0')
