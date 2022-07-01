from django.shortcuts import render, redirect

from marketing.forms import SalesForm,CustomerForm,ProjectForm,BOMForm,SupplierForm
#----------------------------------------------------------------------------------------------

from ERPSystem.models import Sales,Customer,Project,BOM,Supplier

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
                
                return redirect('/marketing/sales')      
            except:  
                traceback.print_exc()
    else:  
        form = SalesForm()  
    return render(request,'marketing_html/index/index_sales.html',{'form':form})  
 

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
        return render(request,'marketing_html/list/sales.html', context)                      

def edit_sales(request,sales_id):  
    sales = Sales.objects.get(sales_id=sales_id)
    return render(request,'marketing_html/edit/edit_sales.html', {'sales':sales,})  

def update_sales(request, sales_id):  
    sales = Sales.objects.get(sales_id=sales_id)
    form = SalesForm(request.POST, instance = sales)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/sales")  
    return render(request,'marketing_html/edit/edit_sales.html', {'sales': sales})  

def destroy_sales(request, sales_id):  
    sales = Sales.objects.get(sales_id=sales_id)
    sales.delete()
    return redirect("/marketing/sales")


def emp_customer(request):  
    if request.method == "POST":   
        form = CustomerForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/marketing/customer')      
            except:  
                traceback.print_exc()
    else:  
        form = CustomerForm()  
    return render(request,'marketing_html/index/index_customer.html',{'form':form})  
   

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
        return render(request,'marketing_html/list/customer.html', context)                      

def edit_customer(request,customer_id):  
    customer = Customer.objects.get(customer_id=customer_id)
    return render(request,'marketing_html/edit/edit_customer.html', {'customer':customer,})  

def update_customer(request, customer_id):  
    customer = Customer.objects.get(customer_id=customer_id)
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/customer")  
    return render(request,'marketing_html/edit/edit_customer.html', {'customer': customer})  

def destroy_customer(request, customer_id):  
    customer = Customer.objects.get(customer_id=customer_id)
    customer.delete()
    return redirect("/marketing/customer")  
    

def emp_supplier(request):  
    if request.method == "POST":   
        form = SupplierForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/marketing/supplier')      
            except:  
                traceback.print_exc()
    else:  
        form = SupplierForm()  
    return render(request,'marketing_html/index/index_supplier.html',{'form':form})  
   

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
        return render(request,'marketing_html/list/supplier.html', context)                      

def edit_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    return render(request,'marketing_html/edit/edit_supplier.html', {'supplier':supplier,})  

def update_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    form = Supplier_01Form(request.POST, instance = supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/supplier")  
    return render(request,'marketing_html/edit/edit_supplier.html', {'supplier': supplier})  

def destroy_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    supplier.delete()
    return redirect("/marketing/supplier") 

#-----------------------------------------------------------------------------
def emp_project(request):  
    if request.method == "POST":   
        form = ProjectForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/marketing/project')      
            except:  
                traceback.print_exc()
    else:  
        form = ProjectForm()  
    return render(request,'marketing_html/index/index_project.html',{'form':form})  
   

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
        return render(request,'marketing_html/list/project.html', context)                      

def edit_project(request, project_id):  
    project = Project.objects.get(project_id=project_id)
    return render(request,'marketing_html/edit/edit_project.html', {'project':project,})  

def update_project(request, project_id):  
    project = Project.objects.get(project_id=project_id)
    form = ProjectForm(request.POST, instance = project)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/project")  
    return render(request,'marketing_html/edit/edit_project.html', {'project': project})  

def destroy_project(request, project_id):  
    project = Product_Reject.objects.get(project_id=project_id)
    project.delete()
    return redirect("/marketing/project")  
#--------------------------------------------------------------------------------
def emp_bom(request):  
    if request.method == "POST":   
        form = BOMForm(request.POST)        
      
        if form.is_valid():  
            try:                 
                form.save()
                return redirect('/marketing/bom')      
            except:  
                traceback.print_exc()
    else:  
        form = BOMForm()  
    return render(request,'marketing_html/index/index_bom.html',{'form':form})  
   

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
        return render(request,'marketing_html/list/bom.html', context)                      
     
def edit_bom(request, bom_id):  
    bom = BOM.objects.get(bom_id=bom_id)
    return render(request,'marketing_html/edit/edit_bom.html', {'bom':bom,})  

def update_bom(request, bom_id):  
    bom = BOM.objects.get(bom_id=bom_id)
    form = BOMForm(request.POST, instance = bom)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/bom")  
    return render(request,'marketing_html/edit/edit_bom.html', {'bom': bom})  

def destroy_bom(request, bom_id):  
    bom = BOM.objects.get(bom_id=bom_id)
    bom.delete()
    return redirect("/marketing/bom")  
#---------------------------------------------------------------------------------------------------------------------

    

  