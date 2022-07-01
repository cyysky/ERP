from django.shortcuts import render, redirect

from purchasing.forms import SupplierForm,Material_SupplierForm,PurchaseForm
#----------------------------------------------------------------------------------------------
from ERPSystem.models import Supplier,Material_Supplier,Purchase

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

def edit_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    return render(request,'purchasing_html/edit/edit_supplier.html', {'supplier':supplier,})  

def update_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
    form = SupplierForm(request.POST, instance = supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/supplier")  
    return render(request,'purchasing_html/edit/edit_supplier.html', {'supplier': supplier})  

def destroy_supplier(request, supplier_id):  
    supplier = Supplier.objects.get(supplier_id=supplier_id)
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

def edit_material_supplier(request, id):  
    material_supplier = Material_Supplier.objects.get(id=id)
    return render(request,'purchasing_html/edit/edit_material_supplier.html', {'material_supplier':material_supplier,})  

def update_material_supplier(request, id):  
    material_supplier = Material_Supplier.objects.get(id=id)
    form = Material_SupplierForm(request.POST, instance = material_supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/material_supplier")  
    return render(request,'purchasing_html/edit/edit_material_supplier.html', {'material_supplier': material_supplier})  

def destroy_material_supplier(request, id):  
    material_supplier = Material_Supplier.objects.get(id=id)
    material_supplier.delete()
    return redirect("/purchasing/material_supplier")

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

def edit_purchase(request, id):  
    purchase = Purchase.objects.get(id=id)
    return render(request,'purchasing_html/edit/edit_purchase.html', {'purchase':purchase,})  

def update_purchase(request, id):  
    purchase = Purchase.objects.get(id=id)
    form = PurchaseForm(request.POST, instance = purchase)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing/purchase")  
    return render(request,'purchasing_html/edit/edit_purchase.html', {'purchase': purchase})  

def destroy_purchase(request, id):  
    purchase = Purchase.objects.get(id=id)
    purchase.delete()
    return redirect("/purchasing/purchase")


