from django.shortcuts import render, redirect

from purchasing.forms import SupplierForm,Material_SupplierForm,PurchaseForm,RequireForm,ReceiveForm
from purchasing.forms import Material_Supplier01Form
#----------------------------------------------------------------------------------------------
from ERPSystem.models import Supplier,Material_Supplier,Purchase,Require,Receive

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

def emp_supplier(request):  
    if request.method == "POST":   
        form = SupplierForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/purchasing/supplier')      
            except:  
                traceback.print_exc()
    else:  
        form = SupplierForm()  
    return render(request,'purchasing_html/index/index_supplier.html',{'form':form})  
   

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
        return render(request,'purchasing_html/list/supplier.html', context)                      

def edit_supplier(request, SupplierID):  
    supplier = Supplier.objects.get(SupplierID=SupplierID)
    return render(request,'purchasing_html/edit/edit_supplier.html', {'supplier':supplier,})  

def update_supplier(request, SupplierID):  
    supplier = Supplier.objects.get(SupplierID=SupplierID)
    form = SupplierForm(request.POST, instance = supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/supplier")  
    return render(request,'purchasing_html/edit/edit_supplier.html', {'supplier': supplier})  

def destroy_supplier(request, SupplierID):  
    supplier = Supplier.objects.get(SupplierID=SupplierID)
    supplier.delete()
    return redirect("/purchasing/supplier") 

#----------------------------------------------------------------------------

def emp_material_supplier(request):  
    if request.method == "POST":   
        form = Material_SupplierForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/purchasing/material_supplier')      
            except:  
                traceback.print_exc()
    else:  
        form = Material_SupplierForm()  
    return render(request,'purchasing_html/index/index_material_supplier.html',{'form':form})  
   

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
        return render(request,'purchasing_html/list/material_supplier.html', context)                      

def edit_material_supplier(request, MaterialSupplierID):  
    material_supplier = Material_Supplier.objects.get(MaterialSupplierID=MaterialSupplierID)
    return render(request,'purchasing_html/edit/edit_material_supplier.html', {'material_supplier':material_supplier,})  

def update_material_supplier(request, MaterialSupplierID):  
    material_supplier = Material_Supplier.objects.get(MaterialSupplierID=MaterialSupplierID)
    form = Material_Supplier01Form(request.POST, instance = material_supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/material_supplier")  
    return render(request,'purchasing_html/edit/edit_material_supplier.html', {'material_supplier': material_supplier})  

def destroy_material_supplier(request, MaterialSupplierID):  
    material_supplier = Material_Supplier.objects.get(MaterialSupplierID=MaterialSupplierID)
    material_supplier.delete()
    return redirect("/purchasing/material_supplier")

#------------------------------------------------------------------------------require

def emp_require(request):  
    if request.method == "POST":   
        form = RequireForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/purchasing/require')      
            except:  
                traceback.print_exc()
    else:  
        form = RequireForm()  
    return render(request,'purchasing_html/index/index_require.html',{'form':form})  
   
def require(request):    
        requires = Require.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(requires,1)
        page = request.GET.get('page1')
        try:
            requires = paginator.page(page)               
        except PageNotAnInteger:
            requires = paginator.page(1)
        except EmptyPage:
            requires = paginator.page(paginator.num_pages)
        context = {'requires': requires,'data' : data}                          
        return render(request,'purchasing_html/list/require.html', context)                      

def edit_require(request, RequireID):  
    require = Require.objects.get(RequireID=RequireID)
    return render(request,'purchasing_html/edit/edit_require.html', {'require':require,})  

def update_require(request, RequireID):  
    require = Require.objects.get(RequireID=RequireID)
    form = RequireForm(request.POST, instance = require)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/require")  
    return render(request,'purchasing_html/edit/edit_require.html', {'require': require})  

def destroy_require(request, RequireID):  
    require = Require.objects.get(RequireID=RequireID)
    require.delete()
    return redirect("/purchasing/require")
#-------------------------------------------------------------------------------------------
def emp_receive(request):  
    if request.method == "POST":   
        form = ReceiveForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/purchasing/receive')      
            except:  
                traceback.print_exc()
    else:  
        form = ReceiveForm()  
    return render(request,'purchasing_html/index/index_receive.html',{'form':form})  
   
def receive(request):    
        receives = Receive.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(receives,1)
        page = request.GET.get('page1')
        try:
            receives = paginator.page(page)               
        except PageNotAnInteger:
            receives = paginator.page(1)
        except EmptyPage:
            receives = paginator.page(paginator.num_pages)
        context = {'receives': receives,'data' : data}                          
        return render(request,'purchasing_html/list/receive.html', context)                      

def edit_receive(request, ReceiveID):  
    receive = Receive.objects.get(ReceiveID=ReceiveID)
    return render(request,'purchasing_html/edit/edit_receive.html', {'receive':receive,})  

def update_receive(request, ReceiveID):  
    receive = Receive.objects.get(ReceiveID=ReceiveID)
    form = ReceiveForm(request.POST, instance = receive)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/receive")  
    return render(request,'purchasing_html/edit/edit_receive.html', {'receive': receive})  

def destroy_receive(request, ReceiveID):  
    receive = Receive.objects.get(ReceiveID=ReceiveID)
    receive.delete()
    return redirect("/purchasing/receive")

#------------------------------------------------------------------------------
def emp_purchase(request):  
    if request.method == "POST":   
        form = PurchaseForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/purchasing/purchase')      
            except:  
                traceback.print_exc()
    else:  
        form = PurchaseForm()  
    return render(request,'purchasing_html/index/index_purchase.html',{'form':form})  
   

def purchase(request):    
        purchases = Purchase.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(purchases,1)
        page = request.GET.get('page1')
        try:
            purchases = paginator.page(page)               
        except PageNotAnInteger:
            purchases = paginator.page(1)
        except EmptyPage:
            purchases = paginator.page(paginator.num_pages)
        context = {'purchases': purchases,'data' : data}                          
        return render(request,'purchasing_html/list/purchase.html', context)                      

def edit_purchase(request, PurchaseID):  
    purchase = Purchase.objects.get(PurchaseID=PurchaseID)
    return render(request,'purchasing_html/edit/edit_purchase.html', {'purchase':purchase,})  

def update_purchase(request, PurchaseID):  
    purchase = Purchase.objects.get(PurchaseID=PurchaseID)
    form = PurchaseForm(request.POST, instance = purchase)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/purchase")  
    return render(request,'purchasing_html/edit/edit_purchase.html', {'purchase': purchase})  

def destroy_purchase(request, PurchaseID):  
    purchase = Purchase.objects.get(PurchaseID=PurchaseID)
    purchase.delete()
    return redirect("/purchasing/purchase")


