from django.db import models
class Sub_contract(models.Model):  
    eid = models.CharField(max_length=20)  #sub_contract
    ename = models.CharField(max_length=100)
    eAddress = models.CharField(max_length=100)  
    eTrem = models.CharField(max_length=100)      
    eemail = models.EmailField(100)  
    ePhone1= models.CharField(max_length=25)
    ePhone2= models.CharField(max_length=25)
    class Meta:  
        db_table = "sub_contract"

class Supplier(models.Model):  
    eida = models.CharField(max_length=20)  #supplier
    enamea = models.CharField(max_length=100)
    eAddressa = models.CharField(max_length=100)  
    eTrema = models.CharField(max_length=100)      
    eemaila = models.EmailField(100)  
    ePhone1a= models.CharField(max_length=25)
    ePhone2a= models.CharField(max_length=25)    
    class Meta:  
        db_table = "supplier"

class Customer(models.Model):  
    eidb = models.CharField(max_length=20)  #customer
    enameb = models.CharField(max_length=100)
    eAddressb = models.CharField(max_length=100)  
    eTremb = models.CharField(max_length=100)      
    eemailb = models.EmailField(100)  
    ePhone1b= models.CharField(max_length=25)
    ePhone2b= models.CharField(max_length=25)
    class Meta:  
        db_table = "customer" 

class Material(models.Model):
    eidb = models.CharField(max_length=20)  #cusnoter
    epart_no = models.CharField(max_length=100)
    egrade = models.CharField(max_length=100)  
    esize = models.CharField(max_length=100)      
    eselect = models.EmailField(100)  
    class Meta:  
        db_table = "material"   
# Create your models here.
