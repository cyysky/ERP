from django.shortcuts import render, redirect
import traceback

from .forms import Product_GoodForm,Product_RejectForm,PackagingForm,DeliveryForm
from .forms import Delivery01Form,Product_Good01Form,Product_Reject01Form

from ERPSystem.models import Product_Good,Product_Reject,Packaging,Delivery
#----------------------------------------
from django.db.models import F, Sum, Window,Avg,OuterRef,Subquery,Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#---------------------------------------------------------------------

def multi_table_view_product_inspection(request):
  packagings = Packaging.objects.all()
  deliverys = Delivery.objects.all()
  context ={'packagings': packagings,
            'deliverys': deliverys,}
  return render(request,'product_inspection_html/multi_table_view_product_inspection.html', context)   

#---------------------------------------------------------------------------
def emp_product_good(request):  
    if request.method == "POST":   
        form = Product_GoodForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/product_inspection/product_good')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_GoodForm()  
    return render(request,'product_inspection_html/index/index_product_good.html',{'form':form})  
   
def product_good(request):    
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["GoodbatchID__contains"] = search_data #  搜索  GoodbatchID  
        product_goods = Product_Good.objects.filter(**data_dict).all()

        paginator = Paginator(product_goods,10)
        page = request.GET.get('page1')
        try:
            product_goods = paginator.page(page)               
        except PageNotAnInteger:
            product_goods = paginator.page(1)
        except EmptyPage:
            product_goods = paginator.page(paginator.num_pages)
        context = {'product_goods': product_goods,'search_data':search_data}                          
        return render(request,'product_inspection_html/list/product_good.html', context)                      

def edit_product_good(request, GoodbatchID):  
    product_good = Product_Good.objects.get(GoodbatchID=GoodbatchID)
    return render(request,'product_inspection_html/edit/edit_product_good.html', {'product_good':product_good,})  

def update_product_good(request, GoodbatchID):  
    product_good = Product_Good.objects.get(GoodbatchID=GoodbatchID)
    form = Product_Good01Form(request.POST, instance = product_good)  
    if form.is_valid():  
        form.save()
        return redirect("/product_inspection/product_good")  
    return render(request,'product_inspection_html/edit/edit_product_good.html', {'product_good': product_good})  

def destroy_product_good(request, GoodbatchID):  
    product_good = Product_Good.objects.get(GoodbatchID=GoodbatchID)
    product_good.delete()
    return redirect("/product_inspection/product_good")

def emp_product_reject(request):  
    if request.method == "POST":   
        form = Product_RejectForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/product_inspection/product_reject')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_RejectForm()  
    return render(request,'product_inspection_html/index/index_product_reject.html',{'form':form})  
   

def product_reject(request):    
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["RejectbatchID__contains"] = search_data #  搜索  RejectbatchID 
        product_rejects = Product_Reject.objects.filter(**data_dict).all()

        paginator = Paginator(product_rejects,10)
        page = request.GET.get('page1')
        try:
            product_rejects = paginator.page(page)               
        except PageNotAnInteger:
            product_rejects = paginator.page(1)
        except EmptyPage:
            product_rejects = paginator.page(paginator.num_pages)
        context = {'product_rejects': product_rejects,'search_data':search_data}                          
        return render(request,'product_inspection_html/list/product_reject.html', context)                      

def edit_product_reject(request, RejectbatchID):  
    product_reject = Product_Reject.objects.get(RejectbatchID=RejectbatchID)
    return render(request,'product_inspection_html/edit/edit_product_reject.html', {'product_reject':product_reject,})  

def update_product_reject(request,RejectbatchID):  
    product_reject = Product_Reject.objects.get(RejectbatchID=RejectbatchID)
    form = Product_Reject01Form(request.POST, instance = product_reject)  
    if form.is_valid():  
        form.save()
        return redirect("/product_inspection/product_reject")  
    return render(request,'product_inspection_html/edit/edit_product_reject.html', {'product_reject': product_reject})  

def destroy_product_reject(request, RejectbatchID):  
    product_reject = Product_Reject.objects.get(RejectbatchID=RejectbatchID)
    product_reject.delete()
    return redirect("/product_inspection/product_reject")  

#----------------------------------------------------------------------------------------------------------------------

def emp_packaging(request):  
    if request.method == "POST":   
        form = PackagingForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/product_inspection/packaging')      
            except:  
                traceback.print_exc()
    else:  
        form = PackagingForm()  
    return render(request,'product_inspection_html/index/index_packaging.html',{'form':form})  
   

def packaging(request):    
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["PackagingID__contains"] = search_data #  搜索  PackagingID 
        packagings = Packaging.objects.filter(**data_dict).all()

        paginator = Paginator(packagings,10)
        page = request.GET.get('page1')
        try:
            packagings = paginator.page(page)               
        except PageNotAnInteger:
            packagings = paginator.page(1)
        except EmptyPage:
            packagings = paginator.page(paginator.num_pages)
        context = {'packagings': packagings,'search_data':search_data}                          
        return render(request,'product_inspection_html/list/packaging.html', context)                      

def edit_packaging(request, PackagingID):  
    packaging = Packaging.objects.get(PackagingID=PackagingID)
    return render(request,'product_inspection_html/edit/edit_packaging.html', {'packaging':packaging,})  

def update_packaging(request, PackagingID):  
    packaging = Packaging.objects.get(PackagingID=PackagingID)
    form = PackagingForm(request.POST, instance = packaging)  
    if form.is_valid():  
        form.save()
        return redirect("/product_inspection/packaging")  
    return render(request,'product_inspection_html/edit/edit_product_reject.html', {'packaging': packaging})  

def destroy_packaging(request, PackagingID):  
    packaging = Packaging.objects.get(PackagingID=PackagingID)
    packaging.delete()
    return redirect("/product_inspection/packaging") 

#---------------------------------------------------------------------------------------------------------------------------------

def emp_delivery(request):  
    if request.method == "POST":   
        form = DeliveryForm(request.POST)        
      
        if form.is_valid():  
            try:                 
                form.save()
                return redirect('/product_inspection/delivery')      
            except:  
                traceback.print_exc()
    else:  
        form = DeliveryForm()  
    return render(request,'product_inspection_html/index/index_delivery.html',{'form':form})  
 
def delivery(request):    
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["DeliveryID__contains"] = search_data #  搜索  DeliveryID 
        deliverys = Delivery.objects.filter(**data_dict).all()
        paginator = Paginator(deliverys,10)
        page = request.GET.get('page1')
        try:
            deliverys = paginator.page(page)               
        except PageNotAnInteger:
            deliverys = paginator.page(1)
        except EmptyPage:
            deliverys = paginator.page(paginator.num_pages)
        context = {'deliverys': deliverys,'search_data':search_data}                          
        return render(request,'product_inspection_html/list/delivery.html', context)                      
     
def edit_delivery(request,DeliveryID):  
    delivery = Delivery.objects.get(DeliveryID=DeliveryID)
    return render(request,'product_inspection_html/edit/edit_delivery.html', {'delivery':delivery,})  

def update_delivery(request,DeliveryID):  
    delivery = Delivery.objects.get(DeliveryID=DeliveryID)
    form = Delivery01Form(request.POST, instance = delivery)  
    if form.is_valid():  
        form.save()
        return redirect("/product_inspection/delivery")  
    return render(request,'product_inspection_html/edit/edit_delivery.html', {'delivery': delivery})  

def destroy_delivery(request,DeliveryID):  
    delivery = delivery.objects.get(DeliveryID=DeliveryID)
    delivery.delete()
    return redirect("/product_inspection/delivery")  

    

  