from django.shortcuts import render, redirect

from warehouse.forms import MaterialForm,Material_StockForm
from warehouse.forms import Material01Form,Material_Stock01Form
#----------------------------------------------------------------------------------------------
from ERPSystem.models import Material,Material_Stock
from ERPSystem.models import Require

#----------------------------------------

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
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["MaterialID__contains"] = search_data    #  搜索  MaterialID 
        materials = Material.objects.filter(**data_dict).values('MaterialID',
                                                                'material_name',
                                                                'measure_unit',
                                                                'tybe',
                                                                'Form',
                                                                'thickness',
                                                                'width',
                                                                'length',
                                                                'pltch',
                                                                'default_stock_locatiuon',
                                                                'quantity',
                                                                'unit_price')
        data = Image.objects.all()  
        paginator = Paginator(materials,10)
        page = request.GET.get('page1')
        try:
            materials = paginator.page(page)               
        except PageNotAnInteger:
            materials = paginator.page(1)
        except EmptyPage:
            materials = paginator.page(paginator.num_pages)
        context = {'materials': materials,'data' : data,"search_data":search_data}                          
        return render(request,'warehouse_html/list/material.html', context)                      

def edit_material(request, MaterialID):  
    material = Material.objects.get(MaterialID=MaterialID)
    return render(request,'warehouse_html/edit/edit_material.html', {'material':material,})  

def update_material(request, MaterialID):  
    material = Material.objects.get(MaterialID=MaterialID)
    form = Material01Form(request.POST, instance = material)  
    if form.is_valid():  
        form.save()
    material = Material.objects.get(MaterialID=MaterialID)
    Require.objects.filter(MaterialID=MaterialID).update(QTY_stock=material.quantity)   
    return render(request,'warehouse_html/edit/edit_material.html', {'material': material})  

def destroy_material(request, MaterialID):  
    material = Material.objects.get(MaterialID=MaterialID)
    material.delete()
    return redirect("/warehouse/material")      

def update_material_to_require(request, MaterialID):  
    material = Material.objects.get(MaterialID=MaterialID)
    if Require.objects.filter(MaterialID=MaterialID) :
         Require.objects.filter(MaterialID=MaterialID).update(QTY_stock=material.quantity)  
         return redirect("/purchasing_material/require")
    else:                
     return redirect("/warehouse/material") 
 #------------------------------------------------------------------------------

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
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["MaterialStockID__contains"] = search_data    #  搜索  MaterialStockID 
        material_stocks = Material_Stock.objects.filter(**data_dict).all()
        data = Image.objects.all()  
        paginator = Paginator(material_stocks,10)
        page = request.GET.get('page1')
        try:
            material_stocks = paginator.page(page)               
        except PageNotAnInteger:
            material_stocks = paginator.page(1)
        except EmptyPage:
            material_stocks = paginator.page(paginator.num_pages)
        context = {'material_stocks': material_stocks,'data' : data,'search_data':search_data}                          
        return render(request,'warehouse_html/list/material_stock.html', context)                      

def edit_material_stock(request, MaterialStockID):  
    material_stock = Material_Stock.objects.get(MaterialStockID=MaterialStockID)
    return render(request,'warehouse_html/edit/edit_material_stock.html', {'material_stock':material_stock,})  

def update_material_stock(request, MaterialStockID):  
    material_stock = Material_Stock.objects.get(MaterialStockID=MaterialStockID)
    form = Material_Stock01Form(request.POST, instance = material_stock)  
    if form.is_valid():  
        form.save()
        return redirect("/warehouse/material_stock")  
    return render(request,'warehouse_html/edit/edit_material_stock.html', {'material_stock': material_stock})  

def destroy_material_stock(request, MaterialStockID):  
    material_stock = Material_Stock.objects.get(MaterialStockID=MaterialStockID)
    material_stock.delete()
    return redirect("/warehouse/material_stock")                            





    

  