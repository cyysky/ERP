from django.shortcuts import render, redirect

from warehouse.forms import MaterialForm,Material_StockForm

#----------------------------------------------------------------------------------------------
from ERPSystem.models import Material,Material_Stock

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
  
   #-------------------------------------------------------------------------------
def emp_material(request):  
    if request.method == "POST":   
        form = MaterialForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/warehouse/material')      
            except:  
                traceback.print_exc()
    else:  
        form = MaterialForm()  
    return render(request,'warehouse_html/index/index_material.html',{'form':form})

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
        return render(request,'warehouse_html/list/material.html', context)                      

def edit_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    return render(request,'warehouse_html/edit/edit_material.html', {'material':material,})  

def update_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    form = MaterialForm(request.POST, instance = material)  
    if form.is_valid():  
        form.save()
        return redirect("/warehouse/material")  
    return render(request,'warehouse_html/edit/edit_material.html', {'material': material})  

def destroy_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    material.delete()
    return redirect("/warehouse/material")      


def emp_material_stock(request):  
    if request.method == "POST":   
        form = Material_StockForm(request.POST)        
        if form.is_valid():  
            try: 
                form.save()             
                return redirect('/warehouse/material_stock')      
            except:  
                traceback.print_exc()
    else:  
        form = Material_StockForm()  
    return render(request,'warehouse_html/index/index_material_stock.html',{'form':form})  
   

def material_stock(request):    
        material_stocks = Material_Stock.objects.all()
        data = Image.objects.all()  
        paginator = Paginator(material_stocks,1)
        page = request.GET.get('page1')
        try:
            material_stocks = paginator.page(page)               
        except PageNotAnInteger:
            material_stocks = paginator.page(1)
        except EmptyPage:
            material_stocks = paginator.page(paginator.num_pages)
        context = {'material_stocks': material_stocks,'data' : data}                          
        return render(request,'warehouse_html/list/material_stock.html', context)                      

def edit_material_stock(request,material_stock_id):  
    material_stock = Material_Stock.objects.get(material_stock_id=material_stock_id)
    return render(request,'warehouse_html/edit/edit_material_stock.html', {'material_stock':material_stock,})  

def update_material_stock(request,material_stock_id):  
    material_stock = Material_Stock.objects.get(material_stock_id=material_stock_id)
    form = Material_StockForm(request.POST, instance = material_stock)  
    if form.is_valid():  
        form.save()
        return redirect("/warehouse/material_stock")  
    return render(request,'warehouse_html/edit/edit_material_stock.html', {'material_stock': material_stock})  

def destroy_material_stock(request,material_stock_id):  
    material_stock = Material_Stock.objects.get(material_stock_id=material_stock_id)
    material_stock.delete()
    return redirect("/warehouse/material_stock") 





    

  