from django.shortcuts import render, redirect

from order.forms import BOMForm,PackagingForm
from order.forms import DeliveryForm

from order.forms import CustomerForm,SupplierForm,SalesForm,ProjectForm
from order.forms import MachineForm,MaterialForm,Material_LocationForm,Material_SupplierForm
from order.forms import ProcessForm,ProductForm,Product_GoodForm,Product_MaterialForm,Product_RejectForm
#----------------------------------------------------------------------------------------------
from order.forms import Supplier_01Form,Sales_01Form
from order.forms import Material_Location_01Form,Material_Supplier_01Form

from order.forms import Process_01Form,Product_01Form,Product_Good_01Form,Product_Material_01Form,Product_Reject_01Form
#----------------------------------------------------------------------------------------------
from employee.models import BOM
from employee.models import Delivery,Packaging

from employee.models import Customer,Supplier,Sales,Project

from employee.models import Machine,Material,Material_Location,Material_Supplier

from employee.models import Process,Product,Product_Good,Product_Material,Product_Reject
#-----------------------------------------没使用或生效的
import sqlite3
import time 
import reportlab
import io
from django import forms
from django.forms import widgets
from django.forms import fields
#----------------------------------------
from datetime    import datetime     # 引入时间模块 
now = datetime.now()
day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute =str(now.minute)
second = str(now.second)
create1 =  day + "-" + month + "-" + year + "__" + hour + ":" + minute + ":" + second

import traceback

from django.db.models import F

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
 
from demo.models import Image

#-------------------------------------------------------------------------
def emp_sales(request):  
    if request.method == "POST":   
        form = SalesForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/sales')      
            except:  
                traceback.print_exc()
    else:  
        form = SalesForm()  
    return render(request,'index/index_sales.html',{'form':form})  
 

def sales(request):    
        saless = Sales.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(saless,4)
        page = request.GET.get('page1')
        try:
            saless = paginator.page(page)               
        except PageNotAnInteger:
            saless = paginator.page(1)
        except EmptyPage:
            saless = paginator.page(paginator.num_pages)
        context = {'saless': saless,'data' : data}                          
        return render(request,'list/sales.html', context)                      

def edit_sales(request,sales_id):  
    sales = Sales.objects.get(sales_id=sales_id)
    return render(request,'edit/edit_sales.html', {'sales':sales,})  

def update_sales(request, sales_id):  
    sales = Sales.objects.get(sales_id=sales_id)
    form = Sales_01Form(request.POST, instance = sales)  
    if form.is_valid():  
        form.save()
        return redirect("/order/sales")  
    return render(request,'edit/edit_sales.html', {'sales': sales})  

def destroy_sales(request, sales_id):  
    sales = Sales.objects.get(sales_id=sales_id)
    sales.delete()
    return redirect("/order/sales")


def emp_customer(request):  
    if request.method == "POST":   
        form = CustomerForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/customer')      
            except:  
                traceback.print_exc()
    else:  
        form = CustomerForm()  
    return render(request,'index/index_customer.html',{'form':form})  
   

def customer(request):    
        customers = Customer.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(customers,1)
        page = request.GET.get('page1')
        try:
            customers = paginator.page(page)               
        except PageNotAnInteger:
            customers = paginator.page(1)
        except EmptyPage:
            customers = paginator.page(paginator.num_pages)
        context = {'customers': customers,'data' : data}                          
        return render(request,'list/customer.html', context)                      

def edit_customer(request,customer_id):  
    customer = Customer.objects.get(customer_id=customer_id)
    return render(request,'edit/edit_customer.html', {'customer':customer,})  

def update_customer(request, customer_id):  
    customer = Customer.objects.get(customer_id=customer_id)
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()
        return redirect("/order/customer")  
    return render(request,'edit/edit_customer.html', {'customer': customer})  

def destroy_customer(request, customer_id):  
    customer = Customer.objects.get(customer_id=customer_id)
    customer.delete()
    return redirect("/order/customer")  
    

def emp_supplier(request):  
    if request.method == "POST":   
        form = SupplierForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/supplier')      
            except:  
                traceback.print_exc()
    else:  
        form = SupplierForm()  
    return render(request,'index/index_supplier.html',{'form':form})  
   

def supplier(request):    
        suppliers = Supplier.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(suppliers,1)
        page = request.GET.get('page1')
        try:
            suppliers = paginator.page(page)               
        except PageNotAnInteger:
            suppliers = paginator.page(1)
        except EmptyPage:
            suppliers = paginator.page(paginator.num_pages)
        context = {'suppliers': suppliers,'data' : data}                          
        return render(request,'list/supplier.html', context)                      

def edit_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    return render(request,'edit/edit_supplier.html', {'supplier':supplier,})  

def update_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    form = Supplier_01Form(request.POST, instance = supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/order/supplier")  
    return render(request,'edit/edit_supplier.html', {'supplier': supplier})  

def destroy_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    supplier.delete()
    return redirect("/order/supplier") 

#-----------------------------------------------------------------------------

def emp_machine(request):  
    if request.method == "POST":   
        form = MachineForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/machine')      
            except:  
                traceback.print_exc()
    else:  
        form = MachineForm()  
    return render(request,'index/index_machine.html',{'form':form})  
   

def machine(request):    
        machines = Machine.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(machines,1)
        page = request.GET.get('page1')
        try:
            machines = paginator.page(page)               
        except PageNotAnInteger:
            machines = paginator.page(1)
        except EmptyPage:
            machines = paginator.page(paginator.num_pages)
        context = {'machines': machines,'data' : data}                          
        return render(request,'list/machine.html', context)                      

def edit_machine(request, machine_id):  
    machine = Machine.objects.get(machine_id=machine_id)
    return render(request,'edit/edit_machine.html', {'machine':machine,})  

def update_machine(request, machine_id):  
    machine = Machine.objects.get(machine_id=machine_id)
    form = MachineForm(request.POST, instance = machine)  
    if form.is_valid():  
        form.save()
        return redirect("/order/machine")  
    return render(request,'edit/edit_machine.html', {'machine': machine})  

def destroy_machine(request, machine_id):  
    machine = Machine.objects.get(machine_id=machine_id)
    machine.delete()
    return redirect("/order/machine")

def emp_material(request):  
    if request.method == "POST":   
        form = MaterialForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/material')      
            except:  
                traceback.print_exc()
    else:  
        form = MaterialForm()  
    return render(request,'index/index_material.html',{'form':form})  
   #-------------------------------------------------------------------------------
def material(request):    
        materials = Material.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(materials,1)
        page = request.GET.get('page1')
        try:
            materials = paginator.page(page)               
        except PageNotAnInteger:
            materials = paginator.page(1)
        except EmptyPage:
            materials = paginator.page(paginator.num_pages)
        context = {'materials': materials,'data' : data}                          
        return render(request,'list/material.html', context)                      

def edit_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    return render(request,'edit/edit_material.html', {'material':material,})  

def update_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    form = MaterialForm(request.POST, instance = material)  
    if form.is_valid():  
        form.save()
        return redirect("/order/material")  
    return render(request,'edit/edit_material.html', {'material': material})  

def destroy_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    material.delete()
    return redirect("/order/material")      



def emp_material_location(request):  
    if request.method == "POST":   
        form = Material_LocationForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/material_location')      
            except:  
                traceback.print_exc()
    else:  
        form = Material_LocationForm()  
    return render(request,'index/index_material_location.html',{'form':form})  
   

def material_location(request):    
        material_locations = Material_Location.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(material_locations,1)
        page = request.GET.get('page1')
        try:
            material_locations = paginator.page(page)               
        except PageNotAnInteger:
            material_locations = paginator.page(1)
        except EmptyPage:
            material_locations = paginator.page(paginator.num_pages)
        context = {'material_locations': material_locations,'data' : data}                          
        return render(request,'list/material_location.html', context)                      

def edit_material_location(request, material_location_id):  
    material_location = Material_Location.objects.get(material_location_id=material_location_id)
    return render(request,'edit/edit_material_location.html', {'material_location':material_location,})  

def update_material_location(request, material_location_id):  
    material_location = Material_Location.objects.get(material_location_id=material_location_id)
    form = Material_Location_01Form(request.POST, instance = material_location)  
    if form.is_valid():  
        form.save()
        return redirect("/order/material_location")  
    return render(request,'edit/edit_material_location.html', {'material_location': material_location})  

def destroy_material_location(request, material_location_id):  
    material_location = Material_Location.objects.get(material_location_id=material_location_id)
    material_location.delete()
    return redirect("/order/material_location") 



def emp_material_supplier(request):  
    if request.method == "POST":   
        form = Material_SupplierForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/material_supplier')      
            except:  
                traceback.print_exc()
    else:  
        form = Material_SupplierForm()  
    return render(request,'index/index_material_supplier.html',{'form':form})  
   

def material_supplier(request):    
        material_suppliers = Material_Supplier.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(material_suppliers,1)
        page = request.GET.get('page1')
        try:
            material_suppliers = paginator.page(page)               
        except PageNotAnInteger:
            material_suppliers = paginator.page(1)
        except EmptyPage:
            material_suppliers = paginator.page(paginator.num_pages)
        context = {'material_suppliers': material_suppliers,'data' : data}                          
        return render(request,'list/material_supplier.html', context)                      

def edit_material_supplier(request, id):  
    material_supplier = Material_Supplier.objects.get(id=id)
    return render(request,'edit/edit_material_supplier.html', {'material_supplier':material_supplier,})  

def update_material_supplier(request, id):  
    material_supplier = Material_Supplier.objects.get(id=id)
    form = Material_Supplier_01Form(request.POST, instance = material_supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/order/material_supplier")  
    return render(request,'edit/edit_material_supplier.html', {'material_supplier': material_supplier})  

def destroy_material_supplier(request, id):  
    material_supplier = Material_Supplier.objects.get(id=id)
    material_supplier.delete()
    return redirect("/order/material_supplier")

#--------------------------------------------------------------------------

def emp_process(request):  
    if request.method == "POST":   
        form = ProcessForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/process')      
            except:  
                traceback.print_exc()
    else:  
        form = ProcessForm()  
    return render(request,'index/index_process.html',{'form':form})  
   

def process(request):    
        processs = Process.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(processs,1)
        page = request.GET.get('page1')
        try:
            processs = paginator.page(page)               
        except PageNotAnInteger:
            processs = paginator.page(1)
        except EmptyPage:
            processs = paginator.page(paginator.num_pages)
        context = {'processs': processs,'data' : data}                          
        return render(request,'list/process.html', context)                      

def edit_process(request, process_id):  
    process = Process.objects.get(process_id=process_id)
    return render(request,'edit/edit_process.html', {'process':process,})  

def update_process(request, process_id):  
    process = Process.objects.get(process_id=process_id)
    form = Process_01Form(request.POST, instance = process)  
    if form.is_valid():  
        form.save()
        return redirect("/order/process")  
    return render(request,'edit/edit_process.html', {'process': process})  

def destroy_process(request, process_id):  
    process = Process.objects.get(process_id=process_id)
    process.delete()
    return redirect("/order/process")  


def emp_product(request):  
    if request.method == "POST":   
        form = ProductForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/product')      
            except:  
                traceback.print_exc()
    else:  
        form =ProductForm()  
    return render(request,'index/index_product.html',{'form':form})  
   

def product(request):    
        products = Product.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(products,1)
        page = request.GET.get('page1')
        try:
            products = paginator.page(page)               
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)
        context = {'products': products,'data' : data}                          
        return render(request,'list/product.html', context)                      

def edit_product(request, product_id):  
    product = Product.objects.get(product_id=product_id)
    return render(request,'edit/edit_product.html', {'product':product,})  

def update_product(request, product_id):  
    product = Product.objects.get(product_id=product_id)
    form = Product_01Form(request.POST, instance = product)  
    if form.is_valid():  
        form.save()
        return redirect("/order/product")  
    return render(request,'edit/edit_product.html', {'product': product})  

def destroy_product(request, product_id):  
    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect("/order/product")  

def emp_product_material(request):  
    if request.method == "POST":   
        form = Product_MaterialForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/product_material')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_MaterialForm()  
    return render(request,'index/index_product_material.html',{'form':form})  
   
def product_material(request):    
        product_materials = Product_Material.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(product_materials,1)
        page = request.GET.get('page1')
        try:
            product_materials = paginator.page(page)               
        except PageNotAnInteger:
            product_materials = paginator.page(1)
        except EmptyPage:
            product_materials = paginator.page(paginator.num_pages)
        context = {'product_materials': product_materials,'data' : data}                          
        return render(request,'list/product_material.html', context)                      

def edit_product_material(request, id):  
    product_material = Product_Material.objects.get(id=id)
    return render(request,'edit/edit_product_material.html', {'product_material':product_material,})  

def update_product_material(request, id):  
    product_material = Product_Material.objects.get(id=id)
    form = Product_Material_01Form(request.POST, instance = product_material)  
    if form.is_valid():  
        form.save()
        return redirect("/order/product_material")  
    return render(request,'edit/edit_product_material.html', {'product_material': product_material})  

def destroy_product_material(request, id):  
    product_material = Product_Material.objects.get(id=id)
    product_material.delete()
    return redirect("/order/product_material")  

def emp_product_good(request):  
    if request.method == "POST":   
        form = Product_GoodForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/product_good')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_GoodForm()  
    return render(request,'index/index_product_good.html',{'form':form})  
   
def product_good(request):    
        product_goods = Product_Good.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(product_goods,1)
        page = request.GET.get('page1')
        try:
            product_goods = paginator.page(page)               
        except PageNotAnInteger:
            product_goods = paginator.page(1)
        except EmptyPage:
            product_goods = paginator.page(paginator.num_pages)
        context = {'product_goods': product_goods,'data' : data}                          
        return render(request,'list/product_good.html', context)                      

def edit_product_good(request, goodbatch_id):  
    product_good = Product_Good.objects.get(goodbatch_id=goodbatch_id)
    return render(request,'edit/edit_product_good.html', {'product_good':product_good,})  

def update_product_good(request, goodbatch_id):  
    product_good = Product_Good.objects.get(goodbatch_id=goodbatch_id)
    form = Product_Good_01Form(request.POST, instance = product_good)  
    if form.is_valid():  
        form.save()
        return redirect("/order/product_good")  
    return render(request,'edit/edit_product_good.html', {'product_good': product_good})  

def destroy_product_good(request, goodbatch_id):  
    product_good = Product_Good.objects.get(goodbatch_id=goodbatch_id)
    product_good.delete()
    return redirect("/order/product_good")

def emp_product_reject(request):  
    if request.method == "POST":   
        form = Product_RejectForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/product_reject')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_RejectForm()  
    return render(request,'index/index_product_reject.html',{'form':form})  
   

def product_reject(request):    
        product_rejects = Product_Reject.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(product_rejects,1)
        page = request.GET.get('page1')
        try:
            product_rejects = paginator.page(page)               
        except PageNotAnInteger:
            product_rejects = paginator.page(1)
        except EmptyPage:
            product_rejects = paginator.page(paginator.num_pages)
        context = {'product_rejects': product_rejects,'data' : data}                          
        return render(request,'list/product_reject.html', context)                      

def edit_product_reject(request, product_reject_id):  
    product_reject = Product_Reject.objects.get(product_reject_id=product_reject_id)
    return render(request,'edit/edit_product_reject.html', {'product_reject':product_reject,})  

def update_product_reject(request, product_reject_id):  
    product_reject = Product_Reject.objects.get(product_reject_id=product_reject_id)
    form = Product_Reject_01Form(request.POST, instance = product_reject)  
    if form.is_valid():  
        form.save()
        return redirect("/order/product_reject")  
    return render(request,'edit/edit_product_reject.html', {'product_reject': product_reject})  

def destroy_product_reject(request, product_reject_id):  
    product_reject = Product_Reject.objects.get(product_reject_id=product_reject_id)
    product_reject.delete()
    return redirect("/order/product_reject")  
#---------------------------------------------------------------------------------------------------------------------

def emp_project(request):  
    if request.method == "POST":   
        form = ProjectForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/project')      
            except:  
                traceback.print_exc()
    else:  
        form = ProjectForm()  
    return render(request,'index/index_project.html',{'form':form})  
   

def project(request):    
        projects = Project.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(projects,1)
        page = request.GET.get('page1')
        try:
            projects = paginator.page(page)               
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)
        context = {'projects': projects,'data' : data}                          
        return render(request,'list/project.html', context)                      

def edit_project(request, project_id):  
    project = Project.objects.get(project_id=project_id)
    return render(request,'edit/edit_project.html', {'product_reject':product_reject,})  

def update_project(request, project_id):  
    project = Project.objects.get(project_id=project_id)
    form = ProjectForm(request.POST, instance = product_reject)  
    if form.is_valid():  
        form.save()
        return redirect("/order/project")  
    return render(request,'edit/edit_project.html', {'project': project})  

def destroy_project(request, project_id):  
    project = Product_Reject.objects.get(project_id=project_id)
    project.delete()
    return redirect("/order/project")  
#--------------------------------------------------------------------------------
def emp_bom(request):  
    if request.method == "POST":   
        form = BOMForm(request.POST)        
      
        if form.is_valid():  
            try:                 
                form.save()
                return redirect('/order/bom')      
            except:  
                traceback.print_exc()
    else:  
        form = BOMForm()  
    return render(request,'index/index_bom.html',{'form':form})  
   

def bom(request):    
        boms = BOM.objects.all()
        data = Image.objects.all()
       #对于date/time字段，可与timedelta()进行运算
       #boms.filter(bom_id=F('product_id')+('material_id'))      
        a=boms.filter(level=F('product_id')+('material_id'))
        #BOM.objects.update(product_id=0,material_id=0,level=a)         
        print(a)
        paginator = Paginator(boms,1)
        page = request.GET.get('page1')
        try:
            boms = paginator.page(page)               
        except PageNotAnInteger:
            boms = paginator.page(1)
        except EmptyPage:
            boms = paginator.page(paginator.num_pages)
        context = {'boms': boms,'data' : data}                          
        return render(request,'list/bom.html', context)                      
     
def edit_bom(request, bom_id):  
    bom = BOM.objects.get(bom_id=bom_id)
    return render(request,'edit/edit_bom.html', {'bom':bom,})  

def update_bom(request, bom_id):  
    bom = BOM.objects.get(bom_id=bom_id)
    form = BOMForm(request.POST, instance = bom)  
    if form.is_valid():  
        form.save()
        return redirect("/order/bom")  
    return render(request,'edit/edit_bom.html', {'bom': bom})  

def destroy_bom(request, bom_id):  
    bom = BOM.objects.get(bom_id=bom_id)
    bom.delete()
    return redirect("/order/bom")  
#---------------------------------------------------------------------------------------------------------------------


def emp_delivery(request):  
    if request.method == "POST":   
        form = DeliveryForm(request.POST)        
      
        if form.is_valid():  
            try:                 
                form.save()
                return redirect('/order/delivery')      
            except:  
                traceback.print_exc()
    else:  
        form = DeliveryForm()  
    return render(request,'index/index_delivery.html',{'form':form})  
 
def delivery(request):    
        deliverys = Delivery.objects.all()
        data = Image.objects.all()
        paginator = Paginator(deliverys,1)
        page = request.GET.get('page1')
        try:
            deliverys = paginator.page(page)               
        except PageNotAnInteger:
            deliverys = paginator.page(1)
        except EmptyPage:
            deliverys = paginator.page(paginator.num_pages)
        context = {'deliverys': deliverys,'data' : data}                          
        return render(request,'list/delivery.html', context)                      
     
def edit_delivery(request,id):  
    delivery = Delivery.objects.get(id=id)
    return render(request,'edit/edit_delivery.html', {'delivery':delivery,})  

def update_delivery(request, id):  
    delivery = Delivery.objects.get(id=id)
    form = DeliveryForm(request.POST, instance = delivery)  
    if form.is_valid():  
        form.save()
        return redirect("/order/delivery")  
    return render(request,'edit/edit_delivery.html', {'delivery': delivery})  

def destroy_delivery(request,id):  
    delivery = delivery.objects.get(id=id)
    delivery.delete()
    return redirect("/order/delivery")  

#----------------------------------------------------------------------------------------------------------------------
def emp_packaging(request):  
    if request.method == "POST":   
        form = PackagingForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/order/packaging')      
            except:  
                traceback.print_exc()
    else:  
        form = PackagingForm()  
    return render(request,'index/index_packaging.html',{'form':form})  
   

def packaging(request):    
        packagings = Packaging.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(packagings,1)
        page = request.GET.get('page1')
        try:
            packagings = paginator.page(page)               
        except PageNotAnInteger:
            packagings = paginator.page(1)
        except EmptyPage:
            packagings = paginator.page(paginator.num_pages)
        context = {'packagings': packagings,'data' : data}                          
        return render(request,'list/packaging.html', context)                      

def edit_packaging(request, id):  
    packaging = Packaging.objects.get(id=id)
    return render(request,'edit/edit_packaging.html', {'packaging':packaging,})  

def update_packaging(request, id):  
    packaging = Packaging.objects.get(id=id)
    form = PackagingForm(request.POST, instance = packaging)  
    if form.is_valid():  
        form.save()
        return redirect("/order/packaging")  
    return render(request,'edit/edit_packaging.html', {'packaging': packaging})  

def destroy_packaging(request, id):  
    packaging = Packaging.objects.get(id=id)
    packaging.delete()
    return redirect("/order/packaging") 

#---------------------------------------------------------------------------------------------------------------------------------

    

  