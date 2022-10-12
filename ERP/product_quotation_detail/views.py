from django.shortcuts import render, redirect
import traceback

from .forms import Sales_OrderForm
from .forms import Sales_Order01Form

from ERPSystem.models import Sales_Order,Product_Sales_Records
#----------------------------------------------------------------------------------------------
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#--------------------------------------------------------------------------------------
def marketing_order(request):
    marketing_order = Sales_Order.objects.all()
    return render(request,'product_quotation_detail_html/list/marketing_order.html',{'marketing_order':marketing_order})  
#---------------------------------------------------------------------------
def emp_sales_order(request):  
    if request.method == "POST":   
        form = Sales_OrderForm(request.POST,request.FILES)# 注意 request.FILES 图片和档案使用       
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/product_quotation_detail/sales_order')      
            except:  
                traceback.print_exc()
    else:  
        form = Sales_OrderForm()  
    return render(request,'product_quotation_detail_html/index/index_sales_order.html',{'form':form})  
 
def sales_order(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["SalesOrderID__contains"] = search_data    #  搜索  SalesOrderID 
        sales_orders = Sales_Order.objects.filter(**data_dict).values('SalesOrderID',
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

        paginator = Paginator(sales_orders,10)
        page = request.GET.get('page1')
        try:
            sales_orders = paginator.page(page)               
        except PageNotAnInteger:
            sales_orders = paginator.page(1)
        except EmptyPage:
            sales_order = paginator.page(paginator.num_pages)
        context = {'sales_orders': sales_orders,'search_data':search_data}                          
        return render(request,'product_quotation_detail_html/list/sales_order.html', context)                      

def edit_sales_order(request,SalesOrderID):  
    sales_order = Sales_Order.objects.get(SalesOrderID=SalesOrderID)
    return render(request,'product_quotation_detail_html/edit/edit_sales_order.html', {'sales_order':sales_order,})  

def update_sales_order(request, SalesOrderID):  
    sales_order = Sales_Order.objects.get(SalesOrderID=SalesOrderID)
    form = Sales_Order01Form(request.POST, instance = sales_order)  
    if form.is_valid():  
        form.save()
        return redirect("/product_quotation_detail/sales_order")  
    return render(request,'product_quotation_detail_html/edit/edit_sales_order.html', {'sales_order': sales_order})  

def destroy_sales_order(request, SalesOrderID):  
    sales_order = Sales_Order.objects.get(SalesOrderID=SalesOrderID)
    # Product_Sales_Records 拿 sales_order 资料--------------------------------------------------------------------------------------------------------------------------
    Product_Sales_Records.objects.create(ProductSalesRecordsID=sales_order.SalesOrderID#ID
                                         ,SalesOrderID=sales_order.SalesOrderID
                                         ,CustomerID=sales_order.CustomerID#Customer object 这字不要,要改
                                         ,customer_name=sales_order.customer_name
                                         ,term=sales_order.term
                                         ,customer_po_id=sales_order.customer_po_id
                                         ,ProductID=sales_order.ProductID#Product object 这字不要,要改 
                                         ,description=sales_order.description
                                         ,quantity=sales_order.quantity
                                         ,unit_price=sales_order.unit_price
                                         ,date=sales_order.date
                                         ,start_time=sales_order.start_time
                                         ,finish_time=sales_order.finish_time
                                         ,title=sales_order.title
                                         ,photo=sales_order.photo)
    sales_order.delete()
    return redirect("/product_quotation_detail/sales_order")

#-----------------------------------------------------------------------------
def product_sales_records(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["SalesOrderID__contains"] = search_data    #  搜索  SalesOrderID 
        product_sales_recordss = Product_Sales_Records.objects.filter(**data_dict).values('SalesOrderID',
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

        paginator = Paginator(product_sales_recordss,10)
        page = request.GET.get('page1')
        try:
            product_sales_recordss = paginator.page(page)               
        except PageNotAnInteger:
            product_sales_recordss = paginator.page(1)
        except EmptyPage:
            product_sales_recordss = paginator.page(paginator.num_pages)
        context = {'product_sales_recordss': product_sales_recordss,'search_data':search_data}                          
        return render(request,'product_quotation_detail_html/list/product_sales_records.html',context) 




  