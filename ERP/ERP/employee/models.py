#from curses import termattrs

from django.db import models
from django.utils import timezone
import uuid
#--------------------------------------------------------------------
class Sales(models.Model):#销售
    sales_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    customer_id = models.ForeignKey(to="Customer",on_delete=models.CASCADE)   #to (customer)customer_id ,customer_name    
    customer_name = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    start_time = models.CharField(max_length=100)
    finish_time = models.CharField(max_length=100)
    customer_po_id = models.CharField(max_length=100)
    #product_id = models.CharField(max_length=100)
    product_id = models.ForeignKey(to="Product",on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    unit_price = models.IntegerField(100000)
    class Meta:  
        db_table = "sales"

class Customer(models.Model):#顾客
    customer_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_name = models.CharField(max_length=100) 
    address = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone1 = models.IntegerField(100000)
    phone2 = models.IntegerField(100000)
    class Meta:  
        db_table = "customer" 

class Supplier(models.Model):#供应商
    supplier_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    supplier_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone1 = models.IntegerField(100000)
    phone2 = models.IntegerField(100000)
    class Meta:  
        db_table = "supplier" 

#--------------------------------------------------------------------机器
class Machine(models.Model):#机器
    machine_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    machine_name = models.CharField(max_length=100)
    unit_price = models.IntegerField(100000)
    class Meta:  
        db_table = "machine" 
#---------------------------------------------------------------------材料      
class Material(models.Model):#材料
    material_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    material_supplier = models.CharField(max_length=100)
    measure_unit = models.CharField(max_length=100)
    tybe = models.CharField(max_length=100)
    Form = models.CharField(max_length=100)
    thickness = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    pltch = models.CharField(max_length=100)
    default_stock_locatiuon = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    nit_price = models.IntegerField(1000)
    class Meta:  
        db_table = "material" 
      
class Material_Location(models.Model):#材料位置
    material_location_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    shelf_id = models.CharField(max_length=100)
    material_id = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True) 
    quantity =  models.IntegerField(100000)
    class Meta:  
        db_table = "material_location"
        
class Material_Supplier(models.Model):#材料供应商
    part_no = models.CharField(max_length=100)
    supplier_id = models.ForeignKey(to="Supplier",on_delete=models.CASCADE)
    class Meta:  
        db_table = "material_supplier" 
#-----------------------------------------------------------------------产品
class Product(models.Model):#产品
    product_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    product_name = models.CharField(max_length=100)
    product_group = models.CharField(max_length=100)
    product_tooling = models.CharField(max_length=100)
    product_unit = models.CharField(max_length=100)
    materil_id = models.CharField(max_length=100)
    material_usage = models.CharField(max_length=100)
    process_id = models.CharField(max_length=100)
    bom_id = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    quantity =  models.IntegerField(100000)
    product_type = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    finish_time = models.CharField(max_length=100)
    unit_price = models.IntegerField(100000)
    class Meta:  
        db_table = "product"

class Process(models.Model):#进程号
    process_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    process_name = models.CharField(max_length=100)
    resource_id  = models.CharField(max_length=100)
    project_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    time  = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=100)
    class Meta:  
        db_table = "process"

class Product_Material(models.Model):#产品材质
    product_id= models.IntegerField(100000)
    material_id = models.IntegerField(100000)
    usage = models.CharField(max_length=100)
    class Meta:  
        db_table = "product_material"
        
class Product_Good(models.Model):#产品好
    goodbatch_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    product_id = models.IntegerField(100000)
    product_name = models.CharField(max_length=100)
    customer_id = models.IntegerField(100000)
    type = models.CharField(max_length=100)
    quantity =  models.IntegerField(100000)
    term = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    material_id = models.IntegerField(100000)
    class Meta:  
        db_table = "product_good"

class Product_Reject(models.Model):#产品不合格
    rejectbatch_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    product_id = models.IntegerField(100000)
    product_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity =  models.IntegerField(100000)
    date = models.DateTimeField(default=timezone.now)
    material_id = models.IntegerField(100000)
    class Meta:  
        db_table = "product_reject"
#------------------------------------------------------------------------------------------project
class Project(models.Model):
    project_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')   
    project_name = models.CharField(max_length=100)
    sales_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    customerpart_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(100000)
    unitprice = models.IntegerField(100000)
    term = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    finish_time = models.CharField(max_length=100)
    class Meta:  
        db_table = "project"

#------------------------------------------------------------------
class BOM(models.Model):
    bom_id = models.CharField(max_length=100,)
    product_id = models.CharField(max_length=100) 
    material_id = models.CharField(max_length=100) 
    level = models.CharField(max_length=100) 
    usage = models.CharField(max_length=100) 
    remarks = models.CharField(max_length=100) 
    class Meta:  
        db_table = "bom" 
#----------------------------------------------------------------------------------------------
class Delivery(models.Model):
    sales_id = models.CharField(max_length=100 )
    sales_name = models.CharField(max_length=100 )
    custiomer_id = models.CharField(max_length=100 )
    product_id = models.CharField(max_length=100 )
    product_name = models.CharField(max_length=100 )
    quantity = models.CharField(max_length=100 )
    unitprice = models.CharField(max_length=100 )
    term = models.CharField(max_length=100 )
    class Meta:
         db_table = "delivery"
#------------------------------------------------------------------------         
class Packaging(models.Model):
    packaging_id= models.CharField(max_length=100)
    packaging_name = models.CharField(max_length=100 )
    packaging_unit = models.CharField(max_length=100 )
    packaging_type = models.CharField(max_length=100 ) 
    packaging_size = models.CharField(max_length=100 )
    packaging_heigh = models.CharField(max_length=100 )
    packaging_width = models.CharField(max_length=100 )
    packaging_length = models.CharField(max_length=100 )
    packaging_color = models.CharField(max_length=100 )
    model = models.CharField(max_length=100 )
    packaging_location  = models.CharField(max_length=100 )
    quantity  = models.CharField(max_length=100 )
    product_company = models.CharField(max_length=100 )
    defaul_stock_location = models.CharField(max_length=100 )
    class Meta:
            db_table= "packaging"
#--------------------------------------------------------------------------------------

class History(models.Model):
    ea0= models.CharField(max_length=100) 
    ea1= models.CharField(max_length=100) 
    ea2= models.CharField(max_length=100)
    ea3= models.CharField(max_length=100)  
    ea4= models.CharField(max_length=100)      
    ea5= models.CharField(max_length=100)
    ea6= models.CharField(max_length=100)
    ea7= models.CharField(max_length=100)
    ea8= models.CharField(max_length=100)
    ea9= models.CharField(max_length=100)
    ea10= models.CharField(max_length=100)  
    ea11= models.CharField(max_length=100)  
    ea12= models.CharField(max_length=100)  
    class Meta:  
        db_table = "history"


# Create your models here.



 



