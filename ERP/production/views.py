from django.shortcuts import render, redirect

from production.forms import ProcessForm,MachineForm,ProductForm,Product_GoodForm,Product_RejectForm,Product_MaterialForm,PackagingForm,DeliveryForm
from production.forms import Delivery01Form,Product_Good01Form,Product_Reject01Form
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

def edit_process(request, ProcessID):  
    process = Process.objects.get(ProcessID=ProcessID)
    return render(request,'production_html/edit/edit_process.html', {'process':process,})  

def update_process(request, ProcessID):  
    process = Process.objects.get(ProcessID=ProcessID)
    form = ProcessForm(request.POST, instance = process)  
    if form.is_valid():  
        form.save()
        return redirect("/production/process")  
    return render(request,'production_html/edit/edit_process.html', {'process': process})  

def destroy_process(request, ProcessID):  
    process = Process.objects.get(ProcessID=ProcessID)
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

def edit_machine(request, MachineID):  
    machine = Machine.objects.get(MachineID=MachineID)
    return render(request,'production_html/edit/edit_machine.html', {'machine':machine,})  

def update_machine(request, MachineID):  
    machine = Machine.objects.get(MachineID=MachineID)
    form = MachineForm(request.POST, instance = machine)  
    if form.is_valid():  
        form.save()
        return redirect("/production/machine")  
    return render(request,'production_html/edit/edit_machine.html', {'machine': machine})  

def destroy_machine(request, MachineID):  
    machine = Machine.objects.get(MachineID=MachineID)
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

def edit_product(request, ProductID):  
    product = Product.objects.get(ProductID=ProductID)
    return render(request,'production_html/edit/edit_product.html', {'product':product,})  

def update_product(request, ProductID):  
    product = Product.objects.get(ProductID=ProductID)
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()
        return redirect("/production/product")  
    return render(request,'production_html/edit/edit_product.html', {'product': product})  

def destroy_product(request, ProductID):  
    product = Product.objects.get(ProductID=ProductID)
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

def edit_product_good(request, GoodbatchID):  
    product_good = Product_Good.objects.get(GoodbatchID=GoodbatchID)
    return render(request,'production_html/edit/edit_product_good.html', {'product_good':product_good,})  

def update_product_good(request, GoodbatchID):  
    product_good = Product_Good.objects.get(GoodbatchID=GoodbatchID)
    form = Product_Good01Form(request.POST, instance = product_good)  
    if form.is_valid():  
        form.save()
        return redirect("/production/product_good")  
    return render(request,'production_html/edit/edit_product_good.html', {'product_good': product_good})  

def destroy_product_good(request, GoodbatchID):  
    product_good = Product_Good.objects.get(GoodbatchID=GoodbatchID)
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

def edit_product_reject(request, RejectbatchID):  
    product_reject = Product_Reject.objects.get(RejectbatchID=RejectbatchID)
    return render(request,'production_html/edit/edit_product_reject.html', {'product_reject':product_reject,})  

def update_product_reject(request,RejectbatchID):  
    product_reject = Product_Reject.objects.get(RejectbatchID=RejectbatchID)
    form = Product_Reject01Form(request.POST, instance = product_reject)  
    if form.is_valid():  
        form.save()
        return redirect("/production/product_reject")  
    return render(request,'production_html/edit/edit_product_reject.html', {'product_reject': product_reject})  

def destroy_product_reject(request, RejectbatchID):  
    product_reject = Product_Reject.objects.get(RejectbatchID=RejectbatchID)
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

def edit_packaging(request, PackagingID):  
    packaging = Packaging.objects.get(PackagingID=PackagingID)
    return render(request,'production_html/edit/edit_packaging.html', {'packaging':packaging,})  

def update_packaging(request, PackagingID):  
    packaging = Packaging.objects.get(PackagingID=PackagingID)
    form = PackagingForm(request.POST, instance = packaging)  
    if form.is_valid():  
        form.save()
        return redirect("/production/packaging")  
    return render(request,'production_html/edit/edit_product_reject.html', {'packaging': packaging})  

def destroy_packaging(request, PackagingID):  
    packaging = Packaging.objects.get(PackagingID=PackagingID)
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
     
def edit_delivery(request,DeliveryID):  
    delivery = Delivery.objects.get(DeliveryID=DeliveryID)
    return render(request,'production_html/edit/edit_delivery.html', {'delivery':delivery,})  

def update_delivery(request,DeliveryID):  
    delivery = Delivery.objects.get(DeliveryID=DeliveryID)
    form = Delivery01Form(request.POST, instance = delivery)  
    if form.is_valid():  
        form.save()
        return redirect("/production/delivery")  
    return render(request,'production_html/edit/edit_delivery.html', {'delivery': delivery})  

def destroy_delivery(request,DeliveryID):  
    delivery = delivery.objects.get(DeliveryID=DeliveryID)
    delivery.delete()
    return redirect("/production/delivery")  

    

  