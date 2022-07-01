from django.shortcuts import render, redirect

from production.forms import ProcessForm,MachineForm,ProductForm,Product_GoodForm,Product_RejectForm,Product_MaterialForm,PackagingForm,DeliveryForm

from ERPSystem.models import Process,Machine,Product,Product_Good,Product_Reject,Product_Material,Packaging,Delivery

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

#--------------------------------------------------------------------------

def emp_process(request):  
    if request.method == "POST":   
        form = ProcessForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/process')      
            except:  
                traceback.print_exc()
    else:  
        form = ProcessForm()  
    return render(request,'production_html/index/index_process.html',{'form':form})  
  
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
        return render(request,'production_html/list/process.html', context)                      

def edit_process(request, process_id):  
    process = Process.objects.get(process_id=process_id)
    return render(request,'production_html/edit/edit_process.html', {'process':process,})  

def update_process(request, process_id):  
    process = Process.objects.get(process_id=process_id)
    form = ProcessForm(request.POST, instance = process)  
    if form.is_valid():  
        form.save()
        return redirect("/production/process")  
    return render(request,'production_html/edit/edit_process.html', {'process': process})  

def destroy_process(request, process_id):  
    process = Process.objects.get(process_id=process_id)
    process.delete()
    return redirect("/production/process")  
#------------------------------------------------------------------------------------------------
def emp_machine(request):  
    if request.method == "POST":   
        form = MachineForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/machine')      
            except:  
                traceback.print_exc()
    else:  
        form = MachineForm()  
    return render(request,'production_html/index/index_machine.html',{'form':form})  
   

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
        return render(request,'production_html/list/machine.html', context)                      

def edit_machine(request, machine_id):  
    machine = Machine.objects.get(machine_id=machine_id)
    return render(request,'production_html/edit/edit_machine.html', {'machine':machine,})  

def update_machine(request, machine_id):  
    machine = Machine.objects.get(machine_id=machine_id)
    form = MachineForm(request.POST, instance = machine)  
    if form.is_valid():  
        form.save()
        return redirect("/production/machine")  
    return render(request,'production_html/edit/edit_machine.html', {'machine': machine})  

def destroy_machine(request, machine_id):  
    machine = Machine.objects.get(machine_id=machine_id)
    machine.delete()
    return redirect("/production/machine")
#----------------------------------------------------------------------------------------------------------------     

def emp_product(request):  
    if request.method == "POST":   
        form = ProductForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/product')      
            except:  
                traceback.print_exc()
    else:  
        form =ProductForm()  
    return render(request,'production_html/index/index_product.html',{'form':form})  
   

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
        return render(request,'production_html/list/product.html', context)                      

def edit_product(request, product_id):  
    product = Product.objects.get(product_id=product_id)
    return render(request,'production_html/edit/edit_product.html', {'product':product,})  

def update_product(request, product_id):  
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()
        return redirect("/production/product")  
    return render(request,'production_html/edit/edit_product.html', {'product': product})  

def destroy_product(request, product_id):  
    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect("/production/product")  

#-----------------------------------------------------------------------------------------------------

def emp_product_material(request):  
    if request.method == "POST":   
        form = Product_MaterialForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/product_material')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_MaterialForm()  
    return render(request,'production_html/index/index_product_material.html',{'form':form})  
   
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
        return render(request,'production_html/list/product_material.html', context)                      

def edit_product_material(request, id):  
    product_material = Product_Material.objects.get(id=id)
    return render(request,'production_html/edit/edit_product_material.html', {'product_material':product_material,})  

def update_product_material(request, id):  
    product_material = Product_Material.objects.get(id=id)
    form = Product_Material_01Form(request.POST, instance = product_material)  
    if form.is_valid():  
        form.save()
        return redirect("/production/product_material")  
    return render(request,'production_html/edit/edit_product_material.html', {'product_material': product_material})  

def destroy_product_material(request, id):  
    product_material = Product_Material.objects.get(id=id)
    product_material.delete()
    return redirect("/production/product_material")  

#-----------------------------------------------------------------------

def emp_material(request):  
    if request.method == "POST":   
        form = MaterialForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/material')      
            except:  
                traceback.print_exc()
    else:  
        form = MaterialForm()  
    return render(request,'production_html/index/index_material.html',{'form':form})  
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
        return render(request,'production_html/list/material.html', context)                      

def edit_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    return render(request,'production_html/edit/edit_material.html', {'material':material,})  

def update_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    form = MaterialForm(request.POST, instance = material)  
    if form.is_valid():  
        form.save()
        return redirect("/production/material")  
    return render(request,'production_html/edit/edit_material.html', {'material': material})  

def destroy_material(request, material_id):  
    material = Material.objects.get(material_id=material_id)
    material.delete()
    return redirect("/production/material") 

#---------------------------------------------------------------------

def emp_product_good(request):  
    if request.method == "POST":   
        form = Product_GoodForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/product_good')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_GoodForm()  
    return render(request,'production_html/index/index_product_good.html',{'form':form})  
   
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
        return render(request,'production_html/list/product_good.html', context)                      

def edit_product_good(request, goodbatch_id):  
    product_good = Product_Good.objects.get(goodbatch_id=goodbatch_id)
    return render(request,'production_html/edit/edit_product_good.html', {'product_good':product_good,})  

def update_product_good(request, goodbatch_id):  
    product_good = Product_Good.objects.get(goodbatch_id=goodbatch_id)
    form = Product_GoodForm(request.POST, instance = product_good)  
    if form.is_valid():  
        form.save()
        return redirect("/production/product_good")  
    return render(request,'production_html/edit/edit_product_good.html', {'product_good': product_good})  

def destroy_product_good(request, goodbatch_id):  
    product_good = Product_Good.objects.get(goodbatch_id=goodbatch_id)
    product_good.delete()
    return redirect("/production/product_good")

def emp_product_reject(request):  
    if request.method == "POST":   
        form = Product_RejectForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/product_reject')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_RejectForm()  
    return render(request,'production_html/index/index_product_reject.html',{'form':form})  
   

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
        return render(request,'production_html/list/product_reject.html', context)                      

def edit_product_reject(request, rejectbatch_id):  
    product_reject = Product_Reject.objects.get(rejectbatch_id=rejectbatch_id)
    return render(request,'production_html/edit/edit_product_reject.html', {'product_reject':product_reject,})  

def update_product_reject(request,rejectbatch_id):  
    product_reject = Product_Reject.objects.get(rejectbatch_id=rejectbatch_id)
    form = Product_RejectForm(request.POST, instance = product_reject)  
    if form.is_valid():  
        form.save()
        return redirect("/production/product_reject")  
    return render(request,'production_html/edit/edit_product_reject.html', {'product_reject': product_reject})  

def destroy_product_reject(request, rejectbatch_id):  
    product_reject = Product_Reject.objects.get(rejectbatch_id=rejectbatch_id)
    product_reject.delete()
    return redirect("/production/product_reject")  

#----------------------------------------------------------------------------------------------------------------------

def emp_packaging(request):  
    if request.method == "POST":   
        form = PackagingForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production/packaging')      
            except:  
                traceback.print_exc()
    else:  
        form = PackagingForm()  
    return render(request,'production_html/index/index_packaging.html',{'form':form})  
   

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
        return render(request,'production_html/list/packaging.html', context)                      

def edit_packaging(request, id):  
    packaging = Packaging.objects.get(id=id)
    return render(request,'production_html/edit/edit_packaging.html', {'packaging':packaging,})  

def update_packaging(request, id):  
    packaging = Packaging.objects.get(id=id)
    form = PackagingForm(request.POST, instance = packaging)  
    if form.is_valid():  
        form.save()
        return redirect("/production/packaging")  
    return render(request,'production_html/edit/edit_product_reject.html', {'packaging': packaging})  

def destroy_packaging(request, id):  
    packaging = Packaging.objects.get(id=id)
    packaging.delete()
    return redirect("/production/packaging") 

#---------------------------------------------------------------------------------------------------------------------------------

def emp_delivery(request):  
    if request.method == "POST":   
        form = DeliveryForm(request.POST)        
      
        if form.is_valid():  
            try:                 
                form.save()
                return redirect('/production/delivery')      
            except:  
                traceback.print_exc()
    else:  
        form = DeliveryForm()  
    return render(request,'production_html/index/index_delivery.html',{'form':form})  
 
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
        return render(request,'production_html/list/delivery.html', context)                      
     
def edit_delivery(request,id):  
    delivery = Delivery.objects.get(id=id)
    return render(request,'production_html/edit/edit_delivery.html', {'delivery':delivery,})  

def update_delivery(request, id):  
    delivery = Delivery.objects.get(id=id)
    form = DeliveryForm(request.POST, instance = delivery)  
    if form.is_valid():  
        form.save()
        return redirect("/production/delivery")  
    return render(request,'production_html/edit/edit_delivery.html', {'delivery': delivery})  

def destroy_delivery(request,id):  
    delivery = delivery.objects.get(id=id)
    delivery.delete()
    return redirect("/production/delivery")  

    

  