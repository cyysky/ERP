from ctypes.wintypes import SIZE
from django.db import models
from django.utils import timezone
#--------------------------------------------------------------------order  
class Sales(models.Model):#销售
    SalesID = models.CharField(max_length=150,primary_key=True)
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.CASCADE,null=True) 
    customer_name = models.CharField(max_length=150)
    term = models.TextField()
    customer_po_id = models.CharField(max_length=150)
    ProductID = models.ForeignKey(to="Product",on_delete=models.CASCADE,null=True) 
    description = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    unit_price = models.IntegerField(150)    
    date = models.DateTimeField(default=timezone.now)
    start_time = models.CharField(max_length=150)
    finish_time = models.CharField(max_length=150)
    class Meta:  
        db_table = "sales"

class Customer(models.Model):#顾客
    CustomerID= models.CharField(max_length=150,primary_key=True)
    customer_name = models.CharField(max_length=150) 
    address_ship = models.TextField()
    address_sold = models.TextField() 
    address_bill = models.TextField()
    term = models.TextField()
    email = models.EmailField(max_length=150)
    phone1 = models.IntegerField(150)
    phone2 = models.IntegerField(150)
    class Meta:  
        db_table = "customer" 
#------------------------------------------------------------------------------------------project
class Project(models.Model):#项目
    ProjectID = models.CharField(max_length=150,primary_key=True)
    project_name = models.CharField(max_length=150)
    SalesID = models.ForeignKey(to="Sales",on_delete=models.CASCADE,null=True) 
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.CASCADE,null=True) 
    customerpart_id = models.CharField(max_length=150)
    ProductID = models.ForeignKey(to="Product",on_delete=models.CASCADE,null=True) 
    product_name = models.CharField(max_length=150)
    quantity = models.IntegerField(150)
    unitprice = models.IntegerField(150)
    project_date = models.IntegerField(150) 
    term = models.CharField(max_length=150)
    start_time = models.CharField(max_length=150)  #时间  edti type="datetime-local"    index  |attr:"type:datetime-local" 
    finish_time = models.CharField(max_length=150)
    DeliveryID = models.CharField(max_length=150)
    DeliveryDatetime = models.CharField(max_length=150)
    class Meta:  
        db_table = "project"

class Process(models.Model):#进程号
    ProcessID= models.CharField(max_length=150,primary_key=True) 
    process_name = models.CharField(max_length=150)
    ResourceID  = models.ForeignKey(to="Resource",on_delete=models.CASCADE,null=True) 
    ProjectID = models.ForeignKey(to="Project",on_delete=models.CASCADE,null=True) 
    ProductID  = models.ForeignKey(to="Product",on_delete=models.CASCADE,null=True) 
    process_tooling = models.CharField(max_length=150)  
    start_time = models.CharField(max_length=150)
    remarks = models.CharField(max_length=150)
    class Meta:  
        db_table = "process"

#------------------------------------------------------------------
class BOM(models.Model):#物料清单
    BOMID = models.CharField(max_length=150,primary_key=True)
    ProductID  = models.ForeignKey(to="Product",on_delete=models.CASCADE,null=True) 
    product_name = models.CharField(max_length=150) 
    MaterialID  = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    material_name = models.CharField(max_length=150) 
    part_number = models.CharField(max_length=150) 
    describe = models.CharField(max_length=150) 
    quantity = models.CharField(max_length=150) 
    unit_of_measurement = models.CharField(max_length=150) 
    usage_type = models.CharField(max_length=150) 
    class Meta:
        db_table = "bom" 

#---------------------------------------------------------------------材料      
class Material(models.Model):#材料
    MaterialID = models.CharField(max_length=150,primary_key=True)
    material_name = models.CharField(max_length=150)
    MaterialSupplierID   = models.ForeignKey(to="Material_Supplier",on_delete=models.CASCADE,null=True) 
    material_supplier_name = models.CharField(max_length=150)
    measure_unit = models.CharField(max_length=150)
    tybe = models.CharField(max_length=150)
    Form = models.CharField(max_length=150)
    thickness = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    length = models.CharField(max_length=150)
    pltch = models.CharField(max_length=150)
    default_stock_locatiuon = models.CharField(max_length=150)
    usage = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    nit_price = models.IntegerField(150)
    class Meta:  
        db_table = "material" 
      
class Material_Stock(models.Model):#材料库存
    MaterialStockID= models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey('Material',on_delete=models.CASCADE,null=True) 
    material_name = models.CharField(max_length=150)
    material_location_id = models.CharField(max_length=150)
    shelf_id = models.CharField(max_length=150)
    quantity = models.IntegerField(150)
    class Meta:  
        db_table = "material_stock"

#----------------------------------------------------------------------------买
class Require(models.Model):#要求 材料 
    RequireID = models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    material_name = models.CharField(max_length=150) 
    ProjectID = models.ForeignKey(to="Project",on_delete=models.CASCADE,null=True) 
    project_name = models.CharField(max_length=150) 
    MaterialSupplierID = models.ForeignKey(to="Material_Supplier",on_delete=models.CASCADE,null=True) 
    material_supplier_name = models.CharField(max_length=150) 
    quantity = models.CharField(max_length=150) 
    class Meta:
        db_table = "require"

class Purchase(models.Model):#交易的记录
    PurchaseID = models.CharField(max_length=150,primary_key=True)
    purchase_name = models.CharField(max_length=150) 
    RequireID= models.ForeignKey(to="Require",on_delete=models.CASCADE,null=True) 
    deliver_date = models.CharField(max_length=150) 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    material_name = models.CharField(max_length=150) 
    quantity = models.CharField(max_length=150) 
    unit_price = models.CharField(max_length=150) 
    discount = models.CharField(max_length=150) 
    total_MYR = models.CharField(max_length=150) 
    remarks = models.CharField(max_length=150) 
    MaterialSupplierID = models.CharField(max_length=150) 
    class Meta:
        db_table = "purchase"


class Material_Supplier(models.Model):#材料供应商(交易信息)
    MaterialSupplierID = models.CharField(max_length=150,primary_key=True)
    SupplierID = models.ForeignKey(to="Supplier",on_delete=models.CASCADE,null=True) 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    material_name = models.CharField(max_length=150) 
    quantity = models.CharField(max_length=150) 
    remarks = models.CharField(max_length=150) 
    class Meta:  
        db_table = "material_supplier" 

class Supplier(models.Model):#供应商()
    SupplierID= models.CharField(max_length=150,primary_key=True)
    supplier_name = models.CharField(max_length=150)
    supplier_type = models.CharField(max_length=150)
    address = models.TextField()
    term = models.TextField()
    email = models.CharField(max_length=150)
    phone1 = models.IntegerField(150)
    phone2 = models.IntegerField(150)
    class Meta:  
        db_table = "supplier" 

class Receive(models.Model):#收到材料
    ReceiveID = models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    SupplierID = models.ForeignKey(to="Supplier",on_delete=models.CASCADE,null=True) 
    grade = models.CharField(max_length=150) 
    size = models.CharField(max_length=150) 
    usage = models.CharField(max_length=150) 
    quantity = models.CharField(max_length=150) 
    remarks = models.CharField(max_length=150) 
    class Meta:
        db_table = "receive"    



#--------------------------------------------------------------------机器
class Resource(models.Model):#资源
    ResourceID = models.CharField(max_length=150,primary_key=True)
    class Meta:
        db_table = "resource"

class Machine(models.Model):#机器
    MachineID= models.CharField(max_length=150,primary_key=True)
    machine_name = models.CharField(max_length=150)
    unit_price = models.IntegerField(150)
    class Meta:  
        db_table = "machine" 
        
#-----------------------------------------------------------------------产品
class Product(models.Model):#产品
    ProductID= models.CharField(max_length=150,primary_key=True)
    product_name = models.CharField(max_length=150)
    product_group = models.CharField(max_length=150)
    product_tooling = models.CharField(max_length=150)
    product_unit = models.CharField(max_length=150)
    MaterialID= models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    material_usage = models.CharField(max_length=150)
    ProjectID = models.ForeignKey(to="Project",on_delete=models.CASCADE,null=True) 
    BOMID = models.ForeignKey(to="BOM",on_delete=models.CASCADE,null=True) 
    date = models.DateTimeField(default=timezone.now)
    quantity =  models.IntegerField(150)
    product_type = models.CharField(max_length=150)
    unit_price = models.IntegerField(150)
    start_time = models.CharField(max_length=150)
    finish_time = models.CharField(max_length=150)
    class Meta:  
        db_table = "product"

class Product_Material(models.Model):#产品材质
    ProductID= models.CharField(max_length=150,primary_key=True)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    usage = models.CharField(max_length=150)
    class Meta:  
        db_table = "product_material"
        
class Product_Good(models.Model):#产品好
    GoodbatchID= models.CharField(max_length=150,primary_key=True)
    ProductID = models.ForeignKey(to="Product",on_delete=models.CASCADE,null=True) 
    product_name = models.CharField(max_length=150)
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.CASCADE,null=True) 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    type  = models.TextField()
    quantity = models.CharField(max_length=150)
    term = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    class Meta:  
        db_table = "product_good"

class Product_Reject(models.Model):#产品不合格
    RejectbatchID= models.CharField(max_length=150,primary_key=True)
    ProductID = models.ForeignKey(to="Product",on_delete=models.CASCADE,null=True) 
    product_name = models.CharField(max_length=150)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.CASCADE,null=True) 
    type = models.TextField()
    quantity= models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    
    class Meta:  
        db_table = "product_reject"

#------------------------------------------------------------------------         
class Packaging(models.Model):#包装产品
    PackagingID = models.CharField(max_length=150,primary_key=True)
    packaging_name = models.CharField(max_length=150)
    packaging_unit = models.CharField(max_length=150)
    packaging_type = models.CharField(max_length=150) 
    size = models.CharField(max_length=150)
    heigh = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    length = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    packaging_location  = models.CharField(max_length=150)
    quantity  = models.CharField(max_length=150)
    product_company = models.CharField(max_length=150)
    defaul_stock_location = models.CharField(max_length=150)
    class Meta:
            db_table= "packaging"

class Delivery(models.Model):#送货
    DeliveryID = models.CharField(max_length=150,primary_key=True)
    SalesID = models.ForeignKey(to="Sales",on_delete=models.CASCADE,null=True) 
    sales_name = models.CharField(max_length=150)
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.CASCADE,null=True) 
    ProductID = models.ForeignKey(to="Product",on_delete=models.CASCADE,null=True) 
    product_name = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    unitprice = models.CharField(max_length=150)
    term = models.TextField()
    DeliveryDatetime = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    class Meta:
         db_table = "delivery"
#--------------------------------------------------------------------------------------
class History(models.Model):
    ea0= models.CharField(max_length=150) 
    ea1= models.CharField(max_length=150) 
    ea2= models.CharField(max_length=150)
    ea3= models.CharField(max_length=150)  
    ea4= models.CharField(max_length=150)      
    ea5= models.CharField(max_length=150)
    ea6= models.CharField(max_length=150)
    ea7= models.CharField(max_length=150)
    ea8= models.CharField(max_length=150)
    ea9= models.CharField(max_length=150)
    ea10= models.CharField(max_length=150)  
    ea11= models.CharField(max_length=150)  
    ea12= models.CharField(max_length=150)  
    class Meta:  
        db_table = "history"

# Create your models here.



 



