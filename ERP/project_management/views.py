from django.shortcuts import render, redirect
import traceback

from .forms import Product_Sales_ItemForm
from .forms import Product_Sales_Item01Form

from ERPSystem.models import Project_Sales_Item
from ERPSystem.models import Require
#----------------------------------------------------------------------------------------------
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#-----------------------------------------------------------------------------

def planning_new_product_projects(request):  
    
    return render(request,'project_management_html/list/planning_new_product_projects.html')  

#-----------------------------------------------------------------------------
def emp_project_sales_item(request):  
    if request.method == "POST":   
        form = Product_Sales_ItemForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/project_management/project_sales_item')      
            except:  
                traceback.print_exc()
    else:  
        form = Product_Sales_ItemForm()  
    return render(request,'project_management_html/index/index_project_sales_item.html',{'form':form})  
   
def project_sales_item(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["ProjectID__contains"] = search_data    #  搜索  ProjectSalesItemID 
        project_sales_items = Project_Sales_Item.objects.filter(**data_dict).values('ProjectSalesItemID',
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

        paginator = Paginator(project_sales_items,10)
        page = request.GET.get('page1')
        try:
            project_sales_items = paginator.page(page)               
        except PageNotAnInteger:
            project_sales_items = paginator.page(1)
        except EmptyPage:
            project_sales_items = paginator.page(paginator.num_pages)
        context = {'project_sales_items': project_sales_items,'search_data':search_data}                          
        return render(request,'project_management_html/list/project_sales_item.html', context)                      

def edit_project_sales_item(request, ProjectSalesItemID):  
    project_sales_item = Project_Sales_Item.objects.get(ProjectSalesItemID=ProjectSalesItemID)
    Require.objects.filter(ProjectSalesItemID=ProjectSalesItemID).update(QTY_project=project_sales_item.quantity)  
    return render(request,'project_management_html/edit/edit_project_sales_item.html', {'project_sales_item':project_sales_item,})  

def update_project_sales_item(request, ProjectSalesItemID):   
    project_sales_item = Project_Sales_Item.objects.get(ProjectSalesItemID=ProjectSalesItemID)
    form = Product_Sales_Item01Form(request.POST, instance = project_sales_item)  
    if form.is_valid():  
        form.save()
    project_sales_item = Project_Sales_Item.objects.get(ProjectSalesItemID=ProjectSalesItemID)
    Require.objects.filter(ProjectSalesItemID=ProjectSalesItemID).update(QTY_project=project_sales_item.quantity)  
    return render(request,'project_management_html/edit/edit_project_sales_item.html', {'project_sales_item': project_sales_item})  

def destroy_project_sales_item(request, ProjectSalesItemID):  
    project_sales_item = Project_Sales_Item.objects.get(ProjectSalesItemID=ProjectSalesItemID)
    project_sales_item.delete()
    return redirect("/project_management/project_sales_item")  

def update_project_to_require(request,ProjectSalesItemID):  #旧版本找ID导入资料保存中.现在的在ERPSystem/views.py
    project_sales_item = Project_Sales_Item.objects.get(ProjectSalesItemID=ProjectSalesItemID)
    if Require.objects.filter(ProjectSalesItemID=ProjectSalesItemID):
        Require.objects.filter(ProjectSalesItemID=ProjectSalesItemID).update(QTY_project=project_sales_item.quantity)  
        return redirect("/purchasing_material/require")#
    else:
        return redirect("/project_management/project_sales_item") 
#--------------------------------------------------------------------------------
   
def project_dashboard(request): 
    
    return render(request,'project_management_html/list/project_dashboard.html') 
  