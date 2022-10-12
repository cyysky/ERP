from django.db import models

class ProductModel(models.Model):
    pname = models.CharField(max_length=100,default='')
    pprice = models.IntengerField(defult=0)
    pimages = models.CharField(max_length=100,default='')
    pdescription = models.TextField(blank=True,default='')
    def __str__ (self):
      return self.pname

class OrdersModel(models.Model):
    subtotal = models.IntengerField(defult=0)
    shipping = models.IntengerField(defult=0)
    grandtotal = models.IntengerField(defult=0)
    customname = models.CharField(max_length=100,default='')
    customemail = models.CharField(max_length=100,default='')
    customaddress = models.CharField(max_length=100,default='')
    customphone = models.CharField(max_length=100,default='')
    paytype = models.CharField(max_length=100,default='')
    def __str__ (self):
      return self.pname

class DetailModel(models.Model):
    droder = models.ForeianKey('OrdersModel',on_delet=models.CASCADE)
    pname = models.CharField(max_length=100,default='')
    unitprce = models.IntengerField(defult=0)
    quantity = models.IntengerField(defult=0)
    dtotal = models.IntengerField(defult=0)
    def __str__ (self):
      return self.pname55