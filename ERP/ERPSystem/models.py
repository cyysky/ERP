from django.db import models
from django.utils import timezone
from django.db.models import Sum
#--------------------------------------------------------------------order  
class Sales(models.Model):#销售
    SalesID = models.CharField(max_length=150,primary_key=True)
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.SET_NULL,null=True) 
    customer_name = models.CharField(max_length=150,default='')
    term = models.TextField()     #rows="4"
    customer_po_id = models.CharField(max_length=150,default='')
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    description = models.CharField(max_length=150,default='')
    quantity = models.CharField(max_length=150,default='')
    unit_price = models.IntegerField()    
    date = models.DateTimeField(default=timezone.now)
    start_time = models.CharField(max_length=150,default='')
    finish_time = models.CharField(max_length=150,default='')
    class Meta:  
        db_table = "sales"

class Customer(models.Model):#顾客
    CustomerID= models.CharField(max_length=150,primary_key=True)
    customer_name = models.CharField(max_length=150,default='') 
    address_ship = models.TextField()
    address_sold = models.TextField() 
    address_bill = models.TextField()
    term = models.TextField()
    email = models.EmailField(max_length=150)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    class Meta:  
        db_table = "customer" 
#------------------------------------------------------------------------------------------project
class Project(models.Model):#项目
    ProjectID = models.CharField(max_length=150,primary_key=True)
    project_name = models.CharField(max_length=150,default='')
    SalesID = models.ForeignKey(to="Sales",on_delete=models.SET_NULL,null=True) 
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.SET_NULL,null=True) 
    customerpart_id = models.CharField(max_length=150,default='')
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    product_name = models.CharField(max_length=150,default='')
    quantity = models.IntegerField(150)
    unitprice = models.IntegerField(150)
    project_date = models.IntegerField() 
    term = models.CharField(max_length=150,default='')
    start_time = models.CharField(max_length=150,default='')  #时间  edti type="datetime-local"    index  |attr:"type:datetime-local" 
    finish_time = models.CharField(max_length=150,default='')
    DeliveryDatetime = models.CharField(max_length=150,default='')
    class Meta:  
        db_table = "project"

class Process(models.Model):#进程号
    ProcessID= models.CharField(max_length=150,primary_key=True) 
    process_name = models.CharField(max_length=150,default='')
    ResourceID  = models.ForeignKey(to="Resource",on_delete=models.SET_NULL,null=True) 
    ProjectID = models.ForeignKey(to="Project",on_delete=models.SET_NULL,null=True) 
    ProductID  = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    process_tooling = models.CharField(max_length=150,default='')  
    start_time = models.CharField(max_length=150,default='')  #时间  edti type="datetime-local"    index  |attr:"type:datetime-local" 
    finish_time = models.CharField(max_length=150,default='')
    duration = models.CharField(max_length=150,default='')
    quanitiy = models.IntegerField(default='')
    unit_price = models.IntegerField(default='')
    cost  = models.IntegerField(default='')
    total= models.IntegerField(default='')
    class Meta:  
        db_table = "process"

#------------------------------------------------------------------
class BOM(models.Model):#物料清单
    BOMID = models.CharField(max_length=150,primary_key=True)
    BOM_Level = models.CharField(max_length=150,default='') 
    ProductID  = models.CharField(max_length=150,default='') 
    product_name = models.CharField(max_length=150,default='') 
    MaterialID  = models.CharField(max_length=150,default='') 
    material_name = models.CharField(max_length=150,default='') 
    source = models.CharField(max_length=150,default='') 
    UOM = models.TextField()
    usage = models.IntegerField()
    unit_price= models.IntegerField()
    remarks = models.CharField(max_length=150,default='')
    amount = models.IntegerField()
    total= models.IntegerField()
    class Meta:
        db_table = "bom" 


class Resource(models.Model):
    ResourceID = models.CharField(max_length=150,primary_key=True)
    reesource_name = models.CharField(max_length=150,default='') 
    remarks = models.CharField(max_length=150,default='') 
    class Meta:
        db_table = "resource"
#---------------------------------------------------------------------材料      
class Material(models.Model):#材料
    MaterialID = models.CharField(max_length=150,primary_key=True)
    material_name = models.CharField(max_length=150,default='')
    measure_unit = models.CharField(max_length=150,default='')
    tybe = models.CharField(max_length=150,default='')
    Form = models.CharField(max_length=150,default='')
    thickness = models.CharField(max_length=150,default='')
    width = models.CharField(max_length=150,default='')
    length = models.CharField(max_length=150,default='')
    pltch = models.CharField(max_length=150,default='')
    default_stock_locatiuon = models.CharField(max_length=150,default='')
    quantity = models.IntegerField()
    unit_price = models.IntegerField()#   material.unit_price   X   BOM.usage  

    class Meta:  
        db_table = "material" 
      
class Material_Stock(models.Model):#材料库存
    MaterialStockID= models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey('Material',on_delete=models.SET_NULL,null=True) 
    material_name = models.CharField(max_length=150,default='')
    material_location_id = models.CharField(max_length=150,default='')
    shelf_id = models.CharField(max_length=150,default='')
    quantity = models.IntegerField(150)
    class Meta:  
        db_table = "material_stock"

#----------------------------------------------------------------------------买
class Require(models.Model):#要求 材料 
    RequireID = models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    material_name = models.CharField(max_length=150,default='') 
    ProjectID = models.ForeignKey(to="Project",on_delete=models.SET_NULL,null=True) 
    project_name = models.CharField(max_length=150,default='') 
    MaterialSupplierID = models.ForeignKey(to="Material_Supplier",on_delete=models.SET_NULL,null=True) 
    material_supplier_name = models.CharField(max_length=150,default='') 
    quantity = models.CharField(max_length=150,default='') 
    class Meta:
        db_table = "require"

class Purchase(models.Model):#交易的记录
    PurchaseID = models.CharField(max_length=150,primary_key=True)
    purchase_name = models.CharField(max_length=150,default='') 
    RequireID= models.ForeignKey(to="Require",on_delete=models.SET_NULL,null=True) 
    deliver_date = models.CharField(max_length=150,default='') 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    material_name = models.CharField(max_length=150,default='') 
    quantity = models.CharField(max_length=150,default='') 
    unit_price = models.CharField(max_length=150,default='') 
    discount = models.CharField(max_length=150,default='') 
    total_MYR = models.CharField(max_length=150,default='') 
    remarks = models.CharField(max_length=150,default='') 
    MaterialSupplierID = models.CharField(max_length=150,default='') 
    class Meta:
        db_table = "purchase"


class Material_Supplier(models.Model):#材料供应商(交易信息)
    MaterialSupplierID = models.CharField(max_length=150,primary_key=True)
    SupplierID = models.ForeignKey(to="Supplier",on_delete=models.SET_NULL,null=True) 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    material_name = models.CharField(max_length=150,default='') 
    source = models.IntegerField() 
    UOM = models.IntegerField() 
    EOQ = models.IntegerField() 
    unit_price = models.IntegerField() 
    term = models.IntegerField() 
    remarks = models.CharField(max_length=150,default='') 
    class Meta:  
        db_table = "material_supplier" 

class Supplier(models.Model):#供应商()
    SupplierID= models.CharField(max_length=150,primary_key=True)
    supplier_name = models.CharField(max_length=150,default='')
    supplier_type = models.CharField(max_length=150,default='')
    address = models.TextField()
    term = models.TextField()
    email = models.CharField(max_length=150,default='')
    phone1 = models.IntegerField(150)
    phone2 = models.IntegerField(150)
    class Meta:  
        db_table = "supplier" 

class Receive(models.Model):#收到材料
    ReceiveID = models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    SupplierID = models.ForeignKey(to="Supplier",on_delete=models.SET_NULL,null=True) 
    grade = models.CharField(max_length=150,default='') 
    size = models.CharField(max_length=150,default='') 
    usage = models.CharField(max_length=150,default='') 
    quantity = models.CharField(max_length=150,default='') 
    remarks = models.CharField(max_length=150,default='') 
    class Meta:
        db_table = "receive"    


#--------------------------------------------------------------------机器

class Machine(models.Model):#机器
    MachineID= models.CharField(max_length=150,primary_key=True)
    machine_name = models.CharField(max_length=150,default='')
    unit_price = models.IntegerField(150)
    class Meta:  
        db_table = "machine" 
        
#-----------------------------------------------------------------------产品
class Product(models.Model):#产品
    ProductID= models.CharField(max_length=150,primary_key=True)
    product_name = models.CharField(max_length=150,default='')
    product_group = models.CharField(max_length=150,default='')
    product_tooling = models.CharField(max_length=150,default='')
    product_unit = models.CharField(max_length=150,default='')
    BOM_Level  = models.CharField(max_length=150,default='')
    date = models.DateTimeField(default=timezone.now)
    quantity =  models.IntegerField(150)
    product_type = models.CharField(max_length=150,default='')
    unit_price = models.IntegerField(150)
    start_time = models.CharField(max_length=150,default='')
    finish_time = models.CharField(max_length=150,default='')
    class Meta:  
        db_table = "product"

class Product_Material(models.Model):#产品材质
    ProductID= models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    usage = models.CharField(max_length=150,default='')
    class Meta:  
        db_table = "product_material"
        
class Product_Good(models.Model):#产品好
    GoodbatchID= models.CharField(max_length=150,primary_key=True)
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    product_name = models.CharField(max_length=150,default='')
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.SET_NULL,null=True) 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    type  = models.TextField()
    quantity = models.CharField(max_length=150,default='')
    term = models.CharField(max_length=150,default='')
    date = models.DateTimeField(default=timezone.now)
    class Meta:  
        db_table = "product_good"

class Product_Reject(models.Model):#产品不合格
    RejectbatchID= models.CharField(max_length=150,primary_key=True)
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    product_name = models.CharField(max_length=150,default='')
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    type = models.TextField()
    quantity= models.CharField(max_length=150,default='')
    date = models.DateTimeField(default=timezone.now)
    
    class Meta:  
        db_table = "product_reject"

#------------------------------------------------------------------------         
class Packaging(models.Model):#包装产品
    PackagingID = models.CharField(max_length=150,primary_key=True)
    packaging_name = models.CharField(max_length=150,default='')
    packaging_unit = models.CharField(max_length=150,default='')
    packaging_type = models.CharField(max_length=150,default='') 
    size = models.CharField(max_length=150,default='')
    heigh = models.CharField(max_length=150,default='')
    width = models.CharField(max_length=150,default='')
    length = models.CharField(max_length=150,default='')
    color = models.CharField(max_length=150,default='')
    model = models.CharField(max_length=150,default='')
    packaging_location  = models.CharField(max_length=150,default='')
    quantity  = models.CharField(max_length=150,default='')
    product_company = models.CharField(max_length=150,default='')
    defaul_stock_location = models.CharField(max_length=150,default='')
    class Meta:
            db_table= "packaging"

class Delivery(models.Model):#送货
    DeliveryID = models.CharField(max_length=150,primary_key=True)
    SalesID = models.ForeignKey(to="Sales",on_delete=models.SET_NULL,null=True) 
    sales_name = models.CharField(max_length=150,default='')
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.SET_NULL,null=True) 
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    product_name = models.CharField(max_length=150,default='')
    quantity = models.CharField(max_length=150,default='')
    unitprice = models.CharField(max_length=150,default='')
    term = models.TextField()
    DeliveryDatetime = models.CharField(max_length=150,default='')
    date = models.DateTimeField(default=timezone.now)
    class Meta:
         db_table = "delivery"
#--------------------------------------------------------------------------------------
class History(models.Model):
    ea0= models.CharField(max_length=150,default='') 
    ea1= models.CharField(max_length=150,default='') 
    ea2= models.CharField(max_length=150,default='')
    ea3= models.CharField(max_length=150,default='')  
    ea4= models.CharField(max_length=150,default='')      
    ea5= models.CharField(max_length=150,default='')
    ea6= models.CharField(max_length=150,default='')
    ea7= models.CharField(max_length=150,default='')
    ea8= models.CharField(max_length=150,default='')
    ea9= models.CharField(max_length=150,default='')
    ea10= models.CharField(max_length=150,default='')  
    ea11= models.CharField(max_length=150,default='')  
    ea12= models.CharField(max_length=150,default='')  
    class Meta:  
        db_table = "history"


# Create your models here.

#class CostCalculationSystem(models.Model):
#    MaterialID= models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
#    Material_UnitPrice= models.IntegerField(1000)
#    BOMID= models.ForeignKey(to="BOM",on_delete=models.SET_NULL,null=True) 
#    BOM_UnitPrice = models.IntegerField(1000)
#    class Meta:  
#        db_table = "cost_calculation_system"

#product
#material.unit price 
#乘上
#BOM.Usage
#得到
#Product的material unit price
 



