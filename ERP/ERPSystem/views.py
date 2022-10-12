from django.shortcuts import render,redirect
import traceback

from .forms import HistoryForm
from .forms import EmployeeForm  
from .forms import Product_QuotationForm,Product_Quotation_ProcessForm,Product_Quotation_MaterialForm,Product_Quotation_Grand_TotalForm

from .models import History
from .models import Employee
from .models import Product_Quotation,Product_Quotation_Process,Product_Quotation_Material
from .models import Product_Quotation_Process_Sub_Total,Product_Quotation_Material_Sub_Total,Product_Quotation_Grand_Total

from .models import Sales_Order,Customer,Project_Sales_Item,BOM
from .models import Material,Material_Stock,Material_Receive

from .models import Supplier,Material_Supplier,Purchase,Require
from .models import Process,Machine,Product,Product_Good,Product_Reject,Product_Material,Packaging,Delivery,Resource
#--------------------------------------------------------------------------------------------------------------------------------
from django.db.models import Sum,Window,F#能从  .objects.all() 拿记录
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#------------------------------------------------保存现在没用的的宣告功能
#import time    
#from django.http import FileResponse
#from django.shortcuts import HttpResponse        
#from datetime    import datetime     # 引入时间模块            
#---------------------------------------------------------- 

def Progress_Table(request):
    data_dict_sales = {}   # 清空
    search_data_sales_order = request.GET.get('search_sales_order',"")                
    if search_data_sales_order:
       data_dict_sales["SalesID__contains"] = search_data_sales_order    #  搜索  SalesOrderID 
    saless = Sales_Order.objects.filter(**data_dict_sales).values('SalesOrderID',
                                  'CustomerID',
                                  'customer_name',
                                  'term',
                                  'customer_po_id',
                                  'ProductID',
                                  'description',
                                  'quantity',
                                  'unit_price',
                                  'date',
                                  'start_time',
                                  'finish_time')

    customers = Customer.objects.all()

    #-----------------------------------------------------------------------------------------
    data_dict_project = {}   # 清空
    search_data_project = request.GET.get('search_project',"")                
    if search_data_project:
       data_dict_project["ProjectID__contains"] = search_data_project    #  搜索  ProjectSalesItemID 
    project_sales_items = Project_Sales_Item.objects.filter(**data_dict_project).values('ProjectSalesItemID',
                                      'project_name',
                                      'SalesOrderID',
                                      'CustomerID',
                                      'customerpart_id',
                                      'ProductID',
                                      'product_name',
                                      'quantity',
                                      'unitprice',
                                      'project_date',
                                      'term',
                                      'start_time',
                                      'finish_time',
                                      'DeliveryDatetime')    
    
    
    machines = Machine.objects.all()

    data_dict_material = {}   # 清空
    search_data_material = request.GET.get('search_material',"")                
    if search_data_material:
       data_dict_material["MaterialID__contains"] = search_data_material  #  搜索   MaterialID
    materials = Material.objects.filter(**data_dict_material).all()

    data_dict_require = {}   # 清空
    search_data_require = request.GET.get('search_require',"")         
    if search_data_require:
       data_dict_require["project_name__contains"] = search_data_require    #  搜索 用project_name 找  ProjectSalesItemID 
    requires = Require.objects.filter(**data_dict_require).values('RequireID',
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
                                       ).order_by("-BOMID")
    

    #packagings = Packaging.object.all()                  'packagings':packagings,
    #---------------------------------------------------------------------------------------------------
    data_dict_product = {}   # 清空
    search_data_product = request.GET.get('search_product',"")                
    if search_data_product:
       data_dict_product["ProductID__contains"] = search_data_product  #  搜索  ProductID 
    products = Product.objects.filter(**data_dict_product).all()
     
    data_dict_process = {}   # 清空
    search_data_process = request.GET.get('search_process',"")                
    if search_data_process:
       data_dict_process["project_name__contains"] = search_data_process  #  搜索  project_name     ProcessID 
    processs= Process.objects.filter(**data_dict_process).values('ProcessID',
                                         'process_name',
                                         'ResourceID',
                                         'ProjectSalesItemID',
                                         'ProductID',
                                         'process_tooling',
                                         'start_time',
                                         'finish_time',
                                         'duration',
                                         'quanitiy',
                                         'unit_price',
                                         'cost'
                                         ).annotate(total=Window(Sum('cost'),order_by=F('ProcessID').asc()))
    #-----------------------------------------------------------------------------------------------------------
    data_dict_purchase = {}   # 清空
    search_data_purchase = request.GET.get('search_purchase',"")                
    if search_data_purchase:
       data_dict_purchase["require_name__contains"] = search_data_purchase
    purchases = Purchase.objects.filter(**data_dict_purchase).values('PurchaseID',
                                            'RequireID',
                                            'MaterialID',
                                            'quantity',
                                            'unit_price',
                                            'discount',
                                            'total_MYR',
                                            'remarks',
                                            'MaterialSupplierID',
                                            'deliver_date')



    suppliers = Supplier.objects.all()
    material_suppliers = Material_Supplier.objects.all()
    product_materials = Product_Material.objects.all()
    deliverys = Delivery.objects.all()

    context = {'saless': saless,
               'customers': customers,
               'project_sales_items':project_sales_items,

               'machines':machines,

               'materials':materials,

               'suppliers':suppliers,
               'material_suppliers':material_suppliers,

               'requires':requires,

               'processs':processs,
               'products':products,
               'product_materials':product_materials,
    
               'purchases':purchases,

               'deliverys':deliverys,

 

               'search_data_sales_order':search_data_sales_order,
               'search_data_project':search_data_project,
               'search_data_product':search_data_product,
               'search_data_process':search_data_process,
               'search_data_material':search_data_material,
               'search_data_require':search_data_require,
               'search_data_purchase':search_data_purchase}
    return render(request,'Progress_Table.html', context)

#--------------------------------------------------------------------

def Selector_Product_Quotation_Detail(request):
  
    return render(request,'Selector_Product_Quotation_Detail.html')


#-------------------------------------------------------------------------------------------
def emp_product_quotation(request):  
    if request.method == "POST":   
        form = Product_QuotationForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/product_quotation_detail')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_QuotationForm()  
    return render(request,'index/index_product_quotation.html',{'form':form})  

def emp_product_quotation_detail_process(request):  
    if request.method == "POST":   
        form = Product_Quotation_ProcessForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/product_quotation_detail')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_Quotation_ProcessForm()  
    return render(request,'index/index_product_quotation_detail_process.html',{'form':form})  

def emp_product_quotation_detail_material(request):  
    if request.method == "POST":   
        form = Product_Quotation_MaterialForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/product_quotation_detail')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_Quotation_MaterialForm()  
    return render(request,'index/index_product_quotation_detail_material.html',{'form':form})  

def product_quotation_detail(request):             #Product_Quotation
    product_quotations = Product_Quotation.objects.values('ProjectSalesItemID','CustomerID','re3','ProductID','SalesOrderID','re6')
    product_quotation_processs = Product_Quotation_Process.objects.values('ProcessID','re8','re9','re10','re11','re12')
    product_quotation_process_sub_totals = Product_Quotation_Process_Sub_Total.objects.all()                 #all Process
    product_quotation_materials = Product_Quotation_Material.objects.values('MaterialID','re19','re20','re21','re22','re23')
    product_quotation_material_sub_totals = Product_Quotation_Material_Sub_Total.objects.all()               #all Material 
    product_quotation_grand_totals = Product_Quotation_Grand_Total.objects.all()                        #all

    context = {'product_quotations':product_quotations,
               'product_quotation_processs':product_quotation_processs,
               'product_quotation_process_sub_totals':product_quotation_process_sub_totals,
               'product_quotation_materials':product_quotation_materials,
               'product_quotation_material_sub_totals':product_quotation_material_sub_totals,
               'product_quotation_grand_totals':product_quotation_grand_totals}
    return render(request,'list/product_quotation_detail.html',context)

def Grand_Total(request):
   product_quotation_process_sub_totals = Product_Quotation_Process_Sub_Total.objects.all()                 #all Process
   product_quotation_material_sub_totals = Product_Quotation_Material_Sub_Total.objects.all()               #all Material 
   product_quotation_grand_totals = Product_Quotation_Grand_Total.objects.all()
   p1=Product_Quotation_Process.objects.all().aggregate(Sum('re8')).get('re8__sum')
   p2=Product_Quotation_Process.objects.all().aggregate(Sum('re9')).get('re9__sum')
   p3=Product_Quotation_Process.objects.all().aggregate(Sum('re10')).get('re10__sum')
   p4=Product_Quotation_Process.objects.all().aggregate(Sum('re11')).get('re11__sum')
   p5=Product_Quotation_Process.objects.all().aggregate(Sum('re12')).get('re12__sum') 
   Product_Quotation_Process_Sub_Total.objects.create(re13=p1,re14=p2,re15=p3,re16=p4,re17=p5)

   m1=Product_Quotation_Material.objects.all().aggregate(Sum('re19')).get('re19__sum')
   m2=Product_Quotation_Material.objects.all().aggregate(Sum('re20')).get('re20__sum')
   m3=Product_Quotation_Material.objects.all().aggregate(Sum('re21')).get('re21__sum')
   m4=Product_Quotation_Material.objects.all().aggregate(Sum('re22')).get('re22__sum')
   m5=Product_Quotation_Material.objects.all().aggregate(Sum('re23')).get('re23__sum')
   Product_Quotation_Material_Sub_Total.objects.create(re24=m1,re25=m2,re26=m3,re27=m4,re28=m5)
   pm1=(p1+m1)
   pm2=(p2+m2)
   pm3=(p3+m3)
   pm4=(p4+m4)
   pm5=(p5+m5)
   Product_Quotation_Grand_Total.objects.create(re30=pm1,re31=pm2,re32=pm3,re33=pm4,re34=pm5)
   context ={  'product_quotation_process_sub_totals':product_quotation_process_sub_totals,
               'product_quotation_material_sub_totals':product_quotation_material_sub_totals,
               'product_quotation_grand_totals':product_quotation_grand_totals}
   if Product_Quotation_Grand_Total.objects.values():
      return redirect('/product_quotation_detail')      
   return render(request,'list/product_quotation_detail.html',context) 

def destroy_product_quotation_detail(request):
   product_quotation_process_sub_total = Product_Quotation_Process_Sub_Total.objects.all()               #all Process
   product_quotation_material_sub_total = Product_Quotation_Material_Sub_Total.objects.all()  
   product_quotation_grand_totals = Product_Quotation_Grand_Total.objects.all()

   product_quotation_process_sub_total.delete()
   product_quotation_material_sub_total.delete() 
   product_quotation_grand_totals.delete()   
   return redirect('/product_quotation_detail') 



   
def edit_product_quotation(request,ProductQuotationID):  
    product_quotation = Product_Quotation.objects.get(ProductQuotationID=ProductQuotationID)
    context = {'product_quotation':product_quotation,}
    return render(request,'/edit/edit_product_quotation_detail.html',context)  

def edit_product_quotation_detail_process(request, id):  
    product_quotation_detail_process = Product_Quotation_Process.objects.get(id=id)
    context = {'product_quotation_detail_process':product_quotation_detail_process,}
    return render(request,'/edit/edit_product_quotation_detail_process.html',context) 

def edit_product_quotation_detail_material(request, id):  
    product_quotation_detail_material = Product_Quotation_Material.objects.get(id=id)
    context ={'product_quotation_detail_material':product_quotation_detail_material,}
    return render(request,'/edit/edit_product_quotation_detail_process.html',context) 
  


def update_product_quotation(request, id):  
    product_quotation = Product_Quotation.objects.get(id=id)
    form = Product_QuotationForm(request.POST, instance = product_quotation)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/product_quotation")  
    context ={'product_quotation':product_quotation,}
    return render(request,'/edit/edit_product_quotation_detail.html',context)  

def update_product_quotation_detail_process(request, id):  
    product_quotation_detail_process = Product_Quotation_Process.objects.get(id=id)
    form = Product_QuotationForm(request.POST, instance = product_quotation_detail_process)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/product_quotation")  
    context ={'product_quotation_detail_process':product_quotation_detail_process,}
    return render(request,'/edit/edit_product_quotation_detail.html',context)  


def update_product_quotation_detail_material(request, id):  
    product_quotation_detail_material = Product_Quotation_Material.objects.get(id=id)
    form = Product_QuotationForm(request.POST, instance = product_quotation_detail_material)  
    if form.is_valid():  
        form.save()
        return redirect("/marketing/product_quotation")  
    context ={'product_quotation_detail_material':product_quotation_detail_material,}
    return render(request,'/edit/edit_product_quotation_detail.html',context)  

def destroy_product_quotation(request):  
    product_quotation = Product_Quotation.objects.all()
    product_quotation.delete()
    return redirect("/product_quotation_detail")

def destroy_product_quotation_detail_process(request):  
    product_quotation_detail_process = Product_Quotation_Process.objects.all()
    product_quotation_detail_process.delete()
    return redirect("/product_quotation_detail")

def destroy_product_quotation_detail_material(request):  
    product_quotation_detail_material = Product_Quotation_Material.objects.all()
    product_quotation_detail_material.delete()
    return redirect("/product_quotation_detail")





#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def REP_mind_map(request):           #这里需要整理
    return render(request,'REP_mind_map.html')


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
    paginator = Paginator(historys,10)
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


#------------------------------------------------------------------------------------------------------------update
#-------------------------------找ID导入资料
def update_to_require(request,RequireID,BOMID,ProjectSalesItemID,MaterialID):  
    Require.objects.get(RequireID=RequireID)    

    bom = BOM.objects.get(BOMID=BOMID)
    if Require.objects.filter(RequireID=RequireID,BOMID=BOMID) :
        Require.objects.filter(RequireID=RequireID,BOMID=BOMID).update( 
                            ProductID=bom.ProductID,
                           product_name=bom.product_name,
                           MaterialID=bom.MaterialID,
                           material_name=bom.material_name
                           ) 
    project_sales_item = Project_Sales_Item.objects.get(ProjectSalesItemID=ProjectSalesItemID)
    if Require.objects.filter(RequireID=RequireID,ProjectSalesItemID=ProjectSalesItemID):
        Require.objects.filter(RequireID=RequireID,ProjectSalesItemID=ProjectSalesItemID).update(QTY_project=project_sales_item.quantity)  

    material = Material.objects.get(MaterialID=MaterialID)
    if Require.objects.filter(RequireID=RequireID,MaterialID=MaterialID) :
         Require.objects.filter(RequireID=RequireID,MaterialID=MaterialID).update(QTY_stock=material.quantity)  
    return redirect("/purchasing_material/require")


def update_to_purchase(request,PurchaseID,RequireID):   
    Purchase.objects.get(PurchaseID=PurchaseID)

    require = Require.objects.get(RequireID=RequireID)
    if Purchase.objects.filter(PurchaseID=PurchaseID,RequireID=RequireID) :
        Purchase.objects.filter(PurchaseID=PurchaseID,RequireID=RequireID).update(MaterialID=require.MaterialID,
                                                                               quantity=require.QTY_purchase) 
    return redirect("/purchasing_material/purchase")  
#-----------------------------------------------------------------------------------------------------


def Website_Layout_Test(request):
    data_dict_material = {}   # 清空
    search_data_material = request.GET.get('search_material',"")                
    if search_data_material:
       data_dict_material["MaterialID__contains"] = search_data_material  #  搜索   MaterialID
    materials = Material.objects.filter(**data_dict_material).all()

    return render(request,'Website_Layout_Test.html',  {'materials':materials})        

#------------------------------------

def qq(request):
  
   return render(request,'57.html')

def zz(request):
  
   return render(request,'zz.html')