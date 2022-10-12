from django.shortcuts import render, redirect
import traceback

from .forms import Material_SupplierForm,RequireForm,PurchaseForm
from .forms import Material_Supplier01Form,Require01Form,Purchase01Form

from ERPSystem.models import Material_Supplier,Require,Purchase,Project_Sales_Item
#----------------------------------------------------------------------------------------------
from django.db.models import Sum,Window,F
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#----------------------------------------------------------------------------
def multi_table_view_purchasing_material(request):
  material_suppliers = Material_Supplier.objects.all()
  requires = Require.objects.all()
  purchases  = Purchase.objects.all()
  context ={'material_suppliers': material_suppliers, 
            'requires': requires,
            'purchases': purchases,}
  return render(request,'purchasing_material_html/multi_table_view_purchasing_material.html', context)   
#---------------------------------------------------------------------------------------------
def emp_material_supplier(request):  
    if request.method == "POST":   
        form = Material_SupplierForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                return redirect('/purchasing_material/material_supplier')      
            except:  
                traceback.print_exc()
    else:  
        form = Material_SupplierForm()  
    return render(request,'purchasing_material_html/index/index_material_supplier.html',{'form':form})  
   

def material_supplier(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["MaterialSupplierID__contains"] = search_data #  搜索  MaterialSupplierID   
        material_suppliers = Material_Supplier.objects.filter(**data_dict).all()

        paginator = Paginator(material_suppliers,10)
        page = request.GET.get('page1')
        try:
            material_suppliers = paginator.page(page)               
        except PageNotAnInteger:
            material_suppliers = paginator.page(1)
        except EmptyPage:
            material_suppliers = paginator.page(paginator.num_pages)
        context = {'material_suppliers': material_suppliers,'search_data':search_data}                          
        return render(request,'purchasing_material_html/list/material_supplier.html', context)                      

def edit_material_supplier(request, MaterialSupplierID):  
    material_supplier = Material_Supplier.objects.get(MaterialSupplierID=MaterialSupplierID)
    return render(request,'purchasing_material_html/edit/edit_material_supplier.html', {'material_supplier':material_supplier,})  

def update_material_supplier(request, MaterialSupplierID):  
    material_supplier = Material_Supplier.objects.get(MaterialSupplierID=MaterialSupplierID)
    form = Material_Supplier01Form(request.POST, instance = material_supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing_material/material_supplier")  
    return render(request,'purchasing_material_html/edit/edit_material_supplier.html', {'material_supplier': material_supplier})  

def destroy_material_supplier(request, MaterialSupplierID):  
    material_supplier = Material_Supplier.objects.get(MaterialSupplierID=MaterialSupplierID)
    material_supplier.delete()
    return redirect("/purchasing_material/material_supplier")


#------------------------------------------------------------------------------require

def emp_require(request):  
    if request.method == "POST":   
        form = RequireForm(request.POST)        
        if form.is_valid():  
            try: 
                form.save()               
                return redirect('/purchasing_material/require')      
            except:  
                traceback.print_exc()
    else:  
        form = RequireForm()
  #      Material.objects.create(quantity=QTY_stock)
  #      ProjectSalesItem.objects.create(quantity=QTY_project)
  #      product_usage * QTY_project = QTY_need  
   #     QTY_need - QTY_stock  = QTY_purchase
    return render(request,'purchasing_material_html/index/index_require.html',{'form':form})  
   
def require(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["RequireID__contains"] = search_data #  搜索  RequireID   
        requires = Require.objects.filter(**data_dict).values('RequireID',
                                          'BOMID',
                                          'ProjectSalesItemID',
                                          'project_name',
                                          'ProductID',
                                          'product_name',
                                          'MaterialID',
                                          'material_name',
                                          'product_usage',
                                          'QTY_project',
                                          'QTY_need',
                                          'QTY_stock',
                                          'remarks',
                                          'quantity',
                                          'QTY_purchase'
                                          ).order_by("-BOMID")#.annotate(QTY_purchase=Window(Sum('QTY_need'),order_by=F('RequireID').asc())).order_by("-RequireID") #,order_by=('ProcessID','ProductID')))
        # connection object
      #  connection_obj = sqlite3.connect('db.sqlite3') # Connecting to sqlite
        # cursor object
     #   cursor_obj = connection_obj.cursor()      
    
     #   cursor_obj.execute("SELECT * FROM requires") 
     #   customer_re=(len(cursor_obj.fetchall()))#customer列表的数量
     #   print(customer_re)
    
     #   cursor_obj.execute("SELECT * FROM requires") 
     #   material_re=(len(cursor_obj.fetchall()))#material列表的数量
     #   print(material_re)
   
     #   connection_obj.commit()
        # Close the connection
    #    connection_obj.close()
         

        if Require.objects.values('ProjectSalesItemID'):
          a=Require.objects.values('ProjectSalesItemID').update(project_name=(F('ProjectSalesItemID')))
          print(a)
        if Require.objects.values('ProductID'):
          b=Require.objects.values('ProductID').update(product_name=(F('ProductID')))
          print(b)
        if Require.objects.values('MaterialID'):
          c=Require.objects.values('MaterialID').update(material_name=(F('MaterialID')))
          print(c)


        paginator = Paginator(requires,10)
        page = request.GET.get('page1')
        try:
            requires = paginator.page(page)               
        except PageNotAnInteger:
            requires = paginator.page(1)
        except EmptyPage:
            requires = paginator.page(paginator.num_pages)
        context = {'requires': requires,'search_data':search_data}                          
        return render(request,'purchasing_material_html/list/require.html', context)                      

def edit_require(request, RequireID):  
    require = Require.objects.get(RequireID=RequireID)
    return render(request,'purchasing_material_html/edit/edit_require.html', {'require':require,})  

def edit_project_sales_item(request, ProjectSalesItemID):  #----------在改中---------------------------------------#
    project_sales_item = Project_Sales_Item.objects.get(ProjectSalesItemID=ProjectSalesItemID)
    return render(request,'project_management_html/edit/edit_project_sales_item.html', {'project_sales_item':project_sales_item,})  

def update_require(request, RequireID):  
    require = Require.objects.get(RequireID=RequireID)
    form = Require01Form(request.POST, instance = require)  
    if form.is_valid():  
        form.save()
    Purchase.objects.filter(RequireID=RequireID) 
    Purchase.objects.filter(RequireID=RequireID).update(MaterialID=require.MaterialID,quantity=require.QTY_purchase)
    return render(request,'purchasing_material_html/edit/edit_require.html', {'require': require})  

def destroy_require(request, RequireID):  
    require = Require.objects.get(RequireID=RequireID)
    require.delete()
    return redirect("/purchasing_material/require")

#------------------------------------------------------------------------------
def emp_purchase(request):  
    if request.method == "POST":   
        form = PurchaseForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/purchasing_material/purchase')      
            except:  
                traceback.print_exc()
    else:  
        form = PurchaseForm()  
    return render(request,'purchasing_material_html/index/index_purchase.html',{'form':form})  
   

def purchase(request):    
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["PurchaseID__contains"] = search_data #  搜索  PurchaseID   
        purchases = Purchase.objects.filter(**data_dict).values('PurchaseID',
                                            'RequireID',
                                            'MaterialID',
                                            'quantity',
                                            'unit_price',
                                            'discount',
                                            'total_MYR',
                                            'remarks',
                                            'MaterialSupplierID',
                                            'deliver_date')

        Purchase.objects.values('PurchaseID',
                                'RequireID',
                                'MaterialID').update(purchase_name=(F('PurchaseID')),
                                                     require_name=(F('RequireID')),
                                                     material_name=(F('MaterialID')))
        paginator = Paginator(purchases,10)
        page = request.GET.get('page1')
        try:
            purchases = paginator.page(page)               
        except PageNotAnInteger:
            purchases = paginator.page(1)
        except EmptyPage:
            purchases = paginator.page(paginator.num_pages)
        context = {'purchases': purchases,'search_data':search_data}                          
        return render(request,'purchasing_material_html/list/purchase.html', context)                      

def edit_purchase(request, PurchaseID):  
    purchase = Purchase.objects.get(PurchaseID=PurchaseID)
    return render(request,'purchasing_material_html/edit/edit_purchase.html', {'purchase':purchase,})  

def update_purchase(request, PurchaseID):  
    purchase = Purchase.objects.get(PurchaseID=PurchaseID)
    form = Purchase01Form(request.POST, instance = purchase)  
    if form.is_valid():  
        form.save()
        return redirect("/purchasing_material/purchase")  
    return render(request,'purchasing_material_html/edit/edit_purchase.html', {'purchase': purchase})  

def destroy_purchase(request, PurchaseID):  
    purchase = Purchase.objects.get(PurchaseID=PurchaseID)
    purchase.delete()
    return redirect("/purchasing_material/purchase")

    

  