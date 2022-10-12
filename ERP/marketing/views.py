from django.shortcuts import render, redirect

from marketing.forms import SalesForm,CustomerForm,ProjectForm,BOMForm
from marketing.forms import Sales01Form,Project01Form
#----------------------------------------------------------------------------------------------

from ERPSystem.models import Sales,Customer,Project,BOM

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

def edit_sales(request,SalesID):  
    sales = Sales.objects.get(SalesID=SalesID)
    return render(request,'marketing_html/edit/edit_sales.html', {'sales':sales,})  

def update_sales(request, SalesID):  
    sales = Sales.objects.get(SalesID=SalesID)
    form = Sales01Form(request.POST, instance = sales)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/sales")  
    return render(request,'marketing_html/edit/edit_sales.html', {'sales': sales})  

def destroy_sales(request, SalesID):  
    sales = Sales.objects.get(SalesID=SalesID)
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

def edit_customer(request,CustomerID):  
    customer = Customer.objects.get(CustomerID=CustomerID)
    return render(request,'marketing_html/edit/edit_customer.html', {'customer':customer,})  

def update_customer(request, CustomerID):  
    customer = Customer.objects.get(CustomerID=CustomerID)
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/customer")  
    return render(request,'marketing_html/edit/edit_customer.html', {'customer': customer})  

def destroy_customer(request, CustomerID):  
    customer = Customer.objects.get(CustomerID=CustomerID)
    customer.delete()
    return redirect("/marketing/customer")  
    

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

def edit_project(request, ProjectID):  
    project = Project.objects.get(ProjectID=ProjectID)
    return render(request,'marketing_html/edit/edit_project.html', {'project':project,})  

def update_project(request, ProjectID):  
    project = Project.objects.get(ProjectID=ProjectID)
    form = Project01Form(request.POST, instance = project)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/project")  
    return render(request,'marketing_html/edit/edit_project.html', {'project': project})  

def destroy_project(request, ProjectID):  
    project = Project.objects.get(ProjectID=ProjectID)
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
        #boms.filter(BOMID=F('ProductID')+('MaterialID'))      
        #a=boms.filter(=F('ProductID')+('MaterialID'))
        #BOM.objects.update(ProductID=0,MaterialID=0,level=a)         
        #print(a)
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
     
def edit_bom(request, BOMID):  
    bom = BOM.objects.get(BOMID=BOMID)
    return render(request,'marketing_html/edit/edit_bom.html', {'bom':bom,})  

def update_bom(request, BOMID):  
    bom = BOM.objects.get(BOMID=BOMID)
    form = BOMForm(request.POST, instance = bom)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/bom")  
    return render(request,'marketing_html/edit/edit_bom.html', {'bom': bom})  

def destroy_bom(request, BOMID):  
    bom = BOM.objects.get(BOMID=BOMID)
    bom.delete()
    return redirect("/marketing/bom")  
#---------------------------------------------------------------------------------------------------------------------

    

  