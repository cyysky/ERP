from django.shortcuts import render,redirect,HttpResponse
from django.db.models import Sum

#--------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------
from ERPSystem.forms import HistoryForm
from ERPSystem.models import History
#------------------------------------------------------------------------------

from ERPSystem.models import BOM,Delivery,Packaging
from ERPSystem.models import Customer,Supplier,Sales,Project
from ERPSystem.models import Machine,Material,Material_Location,Material_Supplier
from ERPSystem.models import Process,Product,Product_Good,Product_Material,Product_Reject
#--------------------------------------------------------------------------------------------------------
from django.http import FileResponse

#from django.http import HttpResponse
from datetime    import datetime     # 引入时间模块 
now = datetime.now()
day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute =str(now.minute)
second = str(now.second)
create1 =  day + "-" + month + "-" + year + "__" + hour + ":" + minute + ":" + second        
#create1 = datetime.datetime.now() 

      
from reportlab.pdfgen import canvas
import sqlite3
import time 
import traceback
import reportlab
import io
from django import forms
from django.forms import widgets
from django.forms import fields
from django.conf import settings       #导入settings
import os                      #创建文件夹需要的包
from django.db.models import F


from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.  


def emp_history(request):  
    if request.method == "POST":  
        form = HistoryForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/history')  
            except:  
                pass  
    else:  
        form = HistoryForm()  
    return render(request,'index/index_history.html',{'form':form})  

def history(request):    
    historys = History.objects.all()
    #re5=History.objects.all().aggregate(Sum('ea9')).get('ea9__sum')
    #print(re5)   
    #re6=History.objects.all().aggregate(Sum('ea10')).get('ea10__sum')
    #print(re6)   
    #re7=History.objects.all().aggregate(Sum('ea11')).get('ea11__sum')
    #print(re7)
    #re8=History.objects.all().aggregate(Sum('ea12')).get('ea12__sum')
    #print(re8)
   #if historys.is_valid():
    #History_Type_Statistics.objects.create(ea0=re5,ea1=re6,ea2=re7,ea3=re8)
    paginator = Paginator(historys,1)
    page = request.GET.get('page1')
    try:
        historys = paginator.page(page)
    except PageNotAnInteger:
        historys = paginator.page(1)
    except EmptyPage:
        historys = paginator.page(paginator.num_pages)
    context = {'historys': historys,}                          
    return render(request,'list/history.html', context)
  
def edit_history(request, id):  
    history = History.objects.get(id=id)  
    return render(request,'edit/edit_history.html', {'history':history})  
def update4(request, id):  
    history = History.objects.get(id=id)  
    form = HistoryForm(request.POST, instance = history)  
    if form.is_valid():  
        form.save()  
        return redirect("/history")  
    return render(request, 'edit/edit_history.html', {'history': history})  
def destroy4(request, id):  
    history = History.objects.get(id=id)  
    history.delete()  
    return redirect("/history")

def main_page(request):
    saless = Sales.objects.all()
    customers = Customer.objects.all()
    suppliers = Supplier.objects.all()

    machines = Machine.objects.all()

    materials = Material.objects.all()
    material_locations = Material_Location.objects.all()
    material_suppliers = Material_Supplier.objects.all()

    products = Product.objects.all()
    processs = Process.objects.all()
    product_materials = Product_Material.objects.all()
    product_goods = Product_Good.objects.all()
    product_rejects = Product_Reject.objects.all()

    context = {'saless': saless,'customers': customers,'suppliers':suppliers,'machines':machines,
               'materials':materials,'material_locations':material_locations,'material_suppliers':material_suppliers,
                'processs':processs,'products':products,'product_materials':product_materials,'product_goods':product_goods,
                    'product_rejects':product_rejects}
    return render(request,'main_page.html', context)

def REP_mind_map(request):
    saless = Sales.objects.all()
    customers = Customer.objects.all()
    suppliers = Supplier.objects.all()

    machines = Machine.objects.all()

    materials = Material.objects.all()
    material_locations = Material_Location.objects.all()
    material_suppliers = Material_Supplier.objects.all()

    products = Product.objects.all()
    processs = Process.objects.all()
    product_materials = Product_Material.objects.all()
    product_goods = Product_Good.objects.all()
    product_rejects = Product_Reject.objects.all()

    context = {'saless': saless,'customers': customers,'suppliers':suppliers,'machines':machines,
               'materials':materials,'material_locations':material_locations,'material_suppliers':material_suppliers,
                'processs':processs,'products':products,'product_materials':product_materials,'product_goods':product_goods,
                    'product_rejects':product_rejects}
    return render(request,'REP_mind_map.html', context)
# Create your views here.

