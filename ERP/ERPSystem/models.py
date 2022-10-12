from django.db import models
from django.utils import timezone
#---------------------------------------------------------
from django.utils.safestring import mark_safe 
from PIL import Image as Im                  # new
#---------------------------------------------------------------------------------保留指令
#  默认值 default=''   
#  可不填写 blank=True           资料可以是没有,显示是null ->  null=True
#  自动建立ID auto_created=True      自动建立ID   .AutoField( primary_key=True)       自己设立 ID 名字 要改其他所有用到ID的
#  时间  DateTimeField()   现在时间 default=timezone.now        
#  在 edti 网站的 type="datetime-local"  在 index 网站的  |attr:"type:datetime-local"    {{ name|date:"Y-m-d H:i:s" }}
#---------------------------------------------------------------------------------所以要再整理(摆放顺序)
#--------------------------------------------------------------------  

#class Marketing_Order(models.Model):#销售 

class Sales_Order(models.Model):#销售 基本资料
    SalesOrderID = models.CharField(max_length=150,primary_key=True)
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.SET_NULL,null=True) 
    customer_name = models.CharField(max_length=150,default='')
    term = models.TextField()     #rows="4"
    customer_po_id = models.CharField(max_length=150,default='')
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    description = models.CharField(max_length=150,default='')
    quantity = models.CharField(max_length=150,default='')
    unit_price = models.IntegerField()    
    title = models.CharField(max_length=150,blank=True ,default='')#图片名字
    photo = models.ImageField(upload_to='pics',default="")  #图片(ps:只能 .png)  w.png 是白图 但 default='pics/w.png'变成图片只能是w.png  要改
    def save(self):                        # new
        super().save()
        img = Im.open(self.photo.path)
        # resize it
        if img.height > 1920 or img.width > 1080:
            output_size = (1920,1080)
            img.thumbnail(output_size)
            img.save(self.photo.path)
    def image_tag(self):                     
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))#图片地址
    date = models.DateTimeField(default=timezone.now)
    start_time = models.CharField(max_length=150,default='') #时间  
    finish_time = models.CharField(max_length=150,default='')#时间  
    class Meta:  
        db_table = "sales_order"

class Product_Sales_Records(models.Model):#记录已完成出销售的资料
    ProductSalesRecordsID = models.CharField(max_length=150,primary_key=True)
    SalesOrderID = models.CharField(max_length=150,default='')
    CustomerID = models.CharField(max_length=150,default='')
    customer_name = models.CharField(max_length=150,default='')
    term = models.TextField()     #rows="4"
    customer_po_id = models.CharField(max_length=150,default='')
    ProductID = models.CharField(max_length=150,default='')
    description = models.CharField(max_length=150,default='')
    quantity = models.CharField(max_length=150,default='')
    unit_price = models.IntegerField()    
    title = models.CharField(max_length=150,blank=True ,default='')#图片名字
    photo = models.ImageField(upload_to='pics',default="")  #图片(ps:只能 .png) pics/w.png 是白图  
    date = models.DateTimeField(default=timezone.now)
    start_time = models.CharField(max_length=150,default='') #时间  
    finish_time = models.CharField(max_length=150,default='')#时间  
    class Meta:  
        db_table = "product_sales_records"
#------------------------------------------------------------------------------------------
class Project_Sales_Item(models.Model):#项目
    ProjectSalesItemID = models.CharField(max_length=150,primary_key=True)
    project_name = models.CharField(max_length=150,default='')
    SalesOrderID = models.ForeignKey(to="Sales_Order",on_delete=models.SET_NULL,null=True) 
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.SET_NULL,null=True) 
    customerpart_id = models.CharField(max_length=150,default='')
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    product_name = models.CharField(max_length=150,default='')
    quantity = models.IntegerField(150)
    unitprice = models.IntegerField(150)
    project_date = models.IntegerField() 
    term = models.CharField(max_length=150,default='')
    start_time = models.CharField(max_length=150,default='')  #时间  
    finish_time = models.CharField(max_length=150,default='') #时间  
    DeliveryDatetime = models.CharField(max_length=150,default='')
    class Meta:  
        db_table = "project_sales_item"
#------------------------------------------------------------------
class BOM(models.Model):#物料清单
    BOMID = models.CharField(max_length=150,primary_key=True)
    BOM_Level = models.CharField(max_length=150,blank=True,default='') 
    ProductID  = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True)  
    product_name = models.CharField(max_length=150,blank=True,default='') 
    MaterialID  = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    material_name = models.CharField(max_length=150,blank=True,default='') 
    source = models.CharField(max_length=150,default='') 
    UOM = models.TextField()
    usage = models.IntegerField()
    unit_price= models.IntegerField()
    remarks = models.CharField(max_length=150,default='')
    amount = models.IntegerField()
    total= models.IntegerField()
    class Meta:
        db_table = "bom"         

class Process(models.Model):#进程号
    ProcessID= models.CharField(max_length=150,primary_key=True) 
    process_name = models.CharField(max_length=150,default='')
    ResourceID  = models.ForeignKey(to="Resource",on_delete=models.SET_NULL,null=True) 
    ProjectSalesItemID = models.ForeignKey(to="Project_Sales_Item",on_delete=models.SET_NULL,null=True) 
    project_name = models.CharField(max_length=150,blank=True,null=True,default='')
    ProductID  = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True) 
    process_tooling = models.CharField(max_length=150,default='')  
    start_time = models.CharField(max_length=150,default='')  #时间 
    finish_time = models.CharField(max_length=150,default='') #时间  
    duration = models.CharField(max_length=150,default='')
    quanitiy = models.IntegerField(default='')
    unit_price = models.IntegerField(default='')
    cost  = models.IntegerField(default='')
    total= models.IntegerField(default='')
    class Meta:  
        db_table = "process"

class Resource(models.Model):#资源             还没设计完  
    ResourceID = models.CharField(max_length=150,primary_key=True)
    reesource_name = models.CharField(max_length=150,default='') 
    remarks = models.CharField(max_length=150,default='') 
    class Meta:
        db_table = "resource"

class Machine(models.Model):#机器                             没设计完
    MachineID= models.CharField(max_length=150,primary_key=True)
    machine_name = models.CharField(max_length=150,default='')
    unit_price = models.IntegerField(150)
    class Meta:  
        db_table = "machine" 
#----------------------------------------------------------------------------------------------------
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
    SalesOrderID = models.ForeignKey(to="Sales_Order",on_delete=models.SET_NULL,null=True) 
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
#---------------------------------------------------------------------------------------
class Employee(models.Model):#员工                没弄好
    EmployeeID = models.CharField(max_length=150,primary_key=True)
    employee_name = models.CharField(max_length=150,default='') 
    SELVALUE = (
    ('male', 'male'), #前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
    ('Female', 'Female'),
    ('secret', 'secret'),
    )
    gender = models.CharField(max_length=150,blank=True,null=True,default='',choices=SELVALUE) 
    ICor_Passport_No = models.IntegerField()
    moblie_contact = models.IntegerField()
    email  = models.EmailField(max_length=150)
    date_birth = models.IntegerField()
    date_join = models.IntegerField()
    hour_rate_RM = models.IntegerField()
    month_rate_RM = models.IntegerField()
    position = models.CharField(max_length=150,default='') 
    level = models.IntegerField()
    department = models.CharField(max_length=150,default='') 
    date_left = models.CharField(max_length=150,default='')  #时间  
    class Meta:  
        db_table = "employee" 

class Customer(models.Model):#顾客
    CustomerID = models.CharField(max_length=150,primary_key=True)
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
    title = models.CharField(max_length=150,blank=True ,default='')#图片名字
    photo = models.ImageField(upload_to='pics',default='')   #图片(ps:只能 .png)
    def save(self):                        # new
        super().save()

        img = Im.open(self.photo.path)

        # resize it
        if img.height > 1920 or img.width > 1080:
            output_size = (1920,1080)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def image_tag(self):                     
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))#图片地址
    class Meta:  
        db_table = "product"

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
#-----------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------
class Require(models.Model):#要求 材料                                                     #可能要 BOM level 来显示摆放顺序 现在再网站显示的是 .order_by("-BOMID")
    RequireID = models.CharField(max_length=150,primary_key=True,)
    BOMID = models.ForeignKey('BOM',on_delete=models.SET_NULL,null=True) 
    ProjectSalesItemID = models.ForeignKey('Project_Sales_Item',on_delete=models.SET_NULL,null=True,default='') 
    project_name = models.CharField(max_length=150,blank=True,null=True,default='') 
    ProductID = models.ForeignKey('Product',on_delete=models.SET_NULL,blank=True,null=True,default='') 
    product_name = models.CharField(max_length=150,blank=True,null=True,default='') 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,blank=True,null=True,default='') 
    material_name = models.CharField(max_length=150,blank=True,null=True,default='')                  
    product_usage = models.IntegerField(default='')   
    QTY_project = models.IntegerField(default='')
    QTY_need = models.IntegerField(default='')
    QTY_stock = models.IntegerField(default='')
    QTY_purchase = models.IntegerField(default='')
    remarks = models.CharField(max_length=150,default='')
    quantity = models.CharField(max_length=150,default=0) 
    class Meta:
        db_table = "require"

class Purchase(models.Model):#交易的记录
    PurchaseID = models.CharField(max_length=150,primary_key=True)
    purchase_name = models.CharField(max_length=150,blank=True,null=True,default='') 
    RequireID= models.ForeignKey(to="Require",on_delete=models.SET_NULL,null=True) 
    require_name= models.CharField(max_length=150,blank=True,null=True,default='') 
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,blank=True,null=True,default=0) 
    material_name = models.CharField(max_length=150,blank=True,null=True,default='') 
    quantity = models.IntegerField(default='')
    unit_price = models.IntegerField(default='')
    discount = models.IntegerField(default='')
    total_MYR = models.IntegerField(default='')
    remarks = models.CharField(max_length=150,default='') 
    MaterialSupplierID = models.ForeignKey(to="Material_Supplier",on_delete=models.SET_NULL,null=True,default='') 
    deliver_date = models.CharField(max_length=150,default='') 
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

class Material_Receive(models.Model):#收到材料
    MaterialReceiveID = models.AutoField( primary_key=True)
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True) 
    SupplierID = models.ForeignKey(to="Supplier",on_delete=models.SET_NULL,null=True) 
    grade = models.CharField(max_length=150,default='') 
    size = models.CharField(max_length=150,default='') 
    usage = models.CharField(max_length=150,default='') 
    quantity = models.CharField(max_length=150,default='') 
    remarks = models.CharField(max_length=150,default='') 
    class Meta:
        db_table = "material_receive"    

#-------------------------------------------------------------------------------------------------------------
class Product_Quotation(models.Model):        #保留 中.....#,blank=True,null=True     #1
    ProjectSalesItemID = models.ForeignKey(to="Project_Sales_Item",on_delete=models.SET_NULL,null=True)
    CustomerID = models.ForeignKey(to="Customer",on_delete=models.SET_NULL,null=True)
    re3 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Delivery Date',default='') 
    ProductID = models.ForeignKey(to="Product",on_delete=models.SET_NULL,null=True)
    SalesOrderID = models.ForeignKey(to="Sales_Order",on_delete=models.SET_NULL,null=True)
    re6 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Order Date',default='') 
    class Meta:  
        db_table = "product_quotation"

class Product_Quotation_Process(models.Model):  #2
    ProcessID = models.ForeignKey(to="Process",on_delete=models.SET_NULL,null=True)
    process_name= models.CharField(max_length=150,blank=True,null=True,default='') 
    re8 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Process RM',default='') 
    re9 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Job Start Time',default='') 
    re10 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Job End Time',default='') 
    re11 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Resources ID',default='') 
    re12 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Person in Charge',default='')
    class Meta:  
        db_table = "product_quotation_process"

class Product_Quotation_Process_Sub_Total(models.Model):    #Sub Total
    re13 = models.CharField(max_length=150,blank=True,null=True,verbose_name='',default='') 
    re14 = models.CharField(max_length=150,blank=True,null=True,verbose_name='',default='') 
    re15 = models.CharField(max_length=150,blank=True,null=True,verbose_name='',default='') 
    re16 = models.CharField(max_length=150,blank=True,null=True,verbose_name='',default='') 
    re17 = models.CharField(max_length=150,blank=True,null=True,verbose_name='',default='') 
    class Meta:  
        db_table = "product_quotation_process_sub_total"

class Product_Quotation_Material(models.Model):  #3
    MaterialID = models.ForeignKey(to="Material",on_delete=models.SET_NULL,null=True)
    material_name= models.CharField(max_length=150,blank=True,null=True,default='') 
    re19 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Material RM',default='') 
    re20 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Stock On Hand',default='') 
    re21 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Stock to Purchase',default='') 
    re22 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Suppliers ID',default='') 
    re23 = models.CharField(max_length=150,blank=True,null=True,verbose_name='Person in Charge',default='')
    class Meta:  
        db_table = "product_quotation_material"
  
class Product_Quotation_Material_Sub_Total(models.Model):    #Sub Total
    re24 = models.CharField(max_length=150,blank=True,null=True,default='') 
    re25 = models.CharField(max_length=150,blank=True,null=True,default='') 
    re26 = models.CharField(max_length=150,blank=True,null=True,default='') 
    re27 = models.CharField(max_length=150,blank=True,null=True,default='') 
    re28 = models.CharField(max_length=150,blank=True,null=True,default='') 
    class Meta:  
        db_table = "product_quotation_material_sub_total"

class Product_Quotation_Grand_Total(models.Model):                                        #4
    re30 = models.CharField(max_length=150,default='') 
    re31 = models.CharField(max_length=150,default='') 
    re32 = models.CharField(max_length=150,default='') 
    re33 = models.CharField(max_length=150,default='') 
    re34 = models.CharField(max_length=150,default='') 
    class Meta:  
        db_table = "product_quotation_grand_total"

class History(models.Model):#---------------------------------------还不可用 没弄好 要重新设计  History 的全部 (网站显示,记录保存,) 
    ea0 = models.CharField(max_length=150,default='') 
    ea1 = models.CharField(max_length=150,default='') 
    ea2 = models.CharField(max_length=150,default='')
    ea3 = models.CharField(max_length=150,default='')  
    ea4 = models.CharField(max_length=150,default='')      
    ea5 = models.CharField(max_length=150,default='')
    ea6 = models.CharField(max_length=150,default='')
    ea7 = models.CharField(max_length=150,default='')
    ea8 = models.CharField(max_length=150,default='')
    ea9 = models.CharField(max_length=150,default='')
    ea10 = models.CharField(max_length=150,default='')  
    ea11 = models.CharField(max_length=150,default='')  
    ea12 = models.CharField(max_length=150,default='')  
    class Meta:  
        db_table = "history"
#-------------------------------------------------------------------------------------保留备注  或  再测试的指令
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
 



