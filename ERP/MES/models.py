from django.db import models

# Create your models here.

class Supplier(models.Model):  
    sid = models.CharField(max_length=20)  
    sname = models.CharField(max_length=100)  
    semail = models.EmailField()  
    scontact1 = models.CharField(max_length=20)
    scontact2 = models.CharField(max_length=20)
    scontact3 = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    class Meta:
        db_table = "supplier"
        
class Customer(models.Model):  
    cid = models.CharField(max_length=20)  
    cname = models.CharField(max_length=100)  
    cemail = models.EmailField()  
    ccontact1 = models.CharField(max_length=20)
    ccontact2 = models.CharField(max_length=20)
    ccontact3 = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    class Meta:
        db_table = "customer"
        
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:
        db_table = "employee"
        
class Material(models.Model):  
    mid = models.CharField(max_length=20)  
    mname = models.CharField(max_length=100)
    mpartno = models.CharField(max_length=100)
    mtype = models.CharField(max_length=100)
    class Meta:
        db_table = "material"