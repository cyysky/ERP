from django.shortcuts import render, redirect

from warehouse.forms import MaterialForm,Material_LocationForm

#----------------------------------------------------------------------------------------------
from ERPSystem.models import Material,Material_Location

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



def emp_material_location(request):  
    if request.method == "POST":   
        form = Material_LocationForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/warehouse/material_location')      
            except:  
                traceback.print_exc()
    else:  
        form = Material_LocationForm()  
    return render(request,'warehouse_html/index/index_material_location.html',{'form':form})  
   

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
        return render(request,'warehouse_html/list/material_location.html', context)                      

def edit_material_location(request, material_location_id):  
    material_location = Material_Location.objects.get(material_location_id=material_location_id)
    return render(request,'warehouse_html/edit/edit_material_location.html', {'material_location':material_location,})  

def update_material_location(request, material_location_id):  
    material_location = Material_Location.objects.get(material_location_id=material_location_id)
    form = Material_Location_01Form(request.POST, instance = material_location)  
    if form.is_valid():  
        form.save()
        return redirect("/warehouse/material_location")  
    return render(request,'warehouse_html/edit/edit_material_location.html', {'material_location': material_location})  

def destroy_material_location(request, material_location_id):  
    material_location = Material_Location.objects.get(material_location_id=material_location_id)
    material_location.delete()
    return redirect("/warehouse/material_location") 





    

  