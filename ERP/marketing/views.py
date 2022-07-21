

from select import select
from django.shortcuts import render, redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from marketing.forms import SalesForm,CustomerForm,ProjectForm,BOMForm
from marketing.forms import Sales01Form,Project01Form,BOM01Form
#----------------------------------------------------------------------------------------------
from ERPSystem.models import Sales,Customer,Project,BOM
from django.db.models import F   
from django.db.models import Q
from django.db.models import Sum

import traceback
from demo.models import Image   #图片功能



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
        paginator = Paginator(customers,10)
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
        paginator = Paginator(projects,10)
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
     #   if BOM.objects.values('ProductID'): 
     #    a=BOM.objects.values('ProductID').annotate(amount=Sum(F('usage') * F('unit_price')))  #得到 所有的,但 update 只可以输入一个
     #    d=BOM.objects.values('ProductID').annotate(total=Sum(F('amount')))
     #    b=a.values('ProductID')
     #    c=a.values('amount')
     #    print(a) 
     #    print(b)
     #    print(c)
     #    print(d)

       #  BOM.objects.values('ProductID').update(amount=(F('usage') * F('unit_price'))) #amount
       #  q=BOM.objects.values('ProductID').annotate(total=Sum(F('amount')))
       #  BOM.objects.values('ProductID').update(total=q)
        # BOM.objects.values('ProductID').update(total=gg)
         
      #   BOM.objects.values('ProductID').update(total=b)
      #   if BOM.objects.values('ProductID'): 
      #    re2=BOM.objects.filter(ProductID=1).aggregate(Sum('amount')).get('amount__sum')
      #    BOM.objects.filter(ProductID=1).update(total=re2)     
      #    re3=BOM.objects.filter(ProductID=2).aggregate(Sum('amount')).get('amount__sum') 
      #    BOM.objects.filter(ProductID=2).update(total=re3)
           
        data = Image.objects.all()
        paginator = Paginator(boms,10)
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
    form = BOM01Form(request.POST, instance = bom)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/bom")  
    return render(request,'marketing_html/edit/edit_bom.html', {'bom': bom})

def destroy_bom(request, BOMID):  
    bom = BOM.objects.get(BOMID=BOMID)
    bom.delete()
    return redirect("/marketing/bom")  

#---------------------------------------------------------------------------------------------------------------------

#                re1=BOM.objects.all().aggregate(Sum('unit_price')).get('unit_price__sum')
#                print(re1)   
#                re2=BOM.objects.all().aggregate(Sum('amount')).get('amount__sum')
#                print(re2)   
#                re3=BOM.objects.all().aggregate(Sum('usage')).get('usage__sum')
#                print(re3)  
#                re4=BOM.objects.all().aggregate(Sum('usage')).get('usage__sum')
#                print(re4) 
#                #---------- P= M1(2)  + M2(4      M1=3  M2=5      
#                #---------- P= M1(2X3)+ M2(4X5) =26  
#                P = lambda re1,re2,re3,re4: re1*re2 + re3*re4
#                print(P(re1,re2,re3,re4))
#                form.save()
#                BOM.objects.update(bom.total)
   

  