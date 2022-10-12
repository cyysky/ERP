from django.shortcuts import render, redirect
import traceback

from .forms import EmployeeForm,CustomerForm,ProductForm,SupplierForm
from .forms import Product01Form

from ERPSystem.models import Employee,Customer,Product,Supplier
#------------------------------------------------------------------------------
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#--------------------------------------------------------------------------------

def multi_table_view_company_information(request):
  employees = Employee.objects.all()
  customers = Customer.objects.all()
  products  = Product.objects.all()
  suppliers = Supplier.objects.all()
  context ={'employees': employees,
            'customers': customers,
            'products': products,
            'suppliers': suppliers,}
  return render(request,'company_information_html/multi_table_view_company_information.html', context)   
#----------------------------------------------------------------------------
def emp_employee(request):  
    if request.method == "POST":   
        form = EmployeeForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                return redirect('/company_information/employee')      
            except:  
                traceback.print_exc()
    else:  
        form = EmployeeForm()  
    return render(request,'company_information_html/index/index_employee.html',{'form':form})  
   
def employee(request): 
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["EmployeeID__contains"] = search_data    #  搜索  CustomerID  
        employees = Employee.objects.filter(**data_dict).all()

        paginator = Paginator(employees,10)
        page = request.GET.get('page1')
        try:
            employees = paginator.page(page)               
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context = {'employees': employees,'search_data':search_data}                          
        return render(request,'company_information_html/list/employee.html', context)                      

def edit_employee(request,EmployeeID):  
    employee = Employee.objects.get(EmployeeID=EmployeeID)
    return render(request,'company_information_html/edit/edit_employee.html', {'employee':employee})  

def update_employee(request, EmployeeID):  
    employee = Employee.objects.get(EmployeeID=EmployeeID)
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()
        return redirect("/company_information/employee")  
    return render(request,'company_information_html/edit/edit_employee.html', {'employee': employee})  

def destroy_employee(request, EmployeeID):  
    employee = Employee.objects.get(EmployeeID=EmployeeID)
    employee.delete()
    return redirect("/company_information/employee")  

#--------------------------------------------------------------------
def emp_customer(request):  
    if request.method == "POST":   
        form = CustomerForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                return redirect('/company_information/customer')      
            except:  
                traceback.print_exc()
    else:  
        form = CustomerForm()  
    return render(request,'company_information_html/index/index_customer.html',{'form':form})  
   
def customer(request): 
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["CustomerID__contains"] = search_data    #  搜索  CustomerID  
        customers = Customer.objects.filter(**data_dict).all()

        paginator = Paginator(customers,10)
        page = request.GET.get('page1')
        try:
            customers = paginator.page(page)               
        except PageNotAnInteger:
            customers = paginator.page(1)
        except EmptyPage:
            customers = paginator.page(paginator.num_pages)
        context = {'customers': customers,'search_data':search_data}                          
        return render(request,'company_information_html/list/customer.html', context)                      

def edit_customer(request,CustomerID):  
    customer = Customer.objects.get(CustomerID=CustomerID)
    return render(request,'company_information_html/edit/edit_customer.html', {'customer':customer,})  

def update_customer(request, CustomerID):  
    customer = Customer.objects.get(CustomerID=CustomerID)
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()
        return redirect("/company_information/customer")  
    return render(request,'company_information_html/edit/edit_customer.html', {'customer': customer})  

def destroy_customer(request, CustomerID):  
    customer = Customer.objects.get(CustomerID=CustomerID)
    customer.delete()
    return redirect("/company_information/customer")  
 
#----------------------------------------------------------------------------------------------------------------     

def emp_product(request):  
    if request.method == "POST":   
        form = ProductForm(request.POST,request.FILES)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/company_information/product')      
            except:  
                traceback.print_exc()
    else:  
        form =ProductForm()  
    return render(request,'company_information_html/index/index_product.html',{'form':form})  
   

def product(request):  
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["ProductID__contains"] = search_data    #  搜索  SalesID 
        products = Product.objects.filter(**data_dict).all().order_by("BOM_Level")

        paginator = Paginator(products,10)
        page = request.GET.get('page1')
        try:
            products = paginator.page(page)               
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)
        context = {'products': products,'search_data':search_data}                          
        return render(request,'company_information_html/list/product.html', context)                      

def edit_product(request, ProductID):  
    product = Product.objects.get(ProductID=ProductID)
    return render(request,'company_information_html/edit/edit_product.html', {'product':product,})  

def update_product(request, ProductID):  
    product = Product.objects.get(ProductID=ProductID)
    form = Product01Form(request.POST, instance = product)  
    if form.is_valid():  
        form.save()
        return redirect("/company_information/product")  
    return render(request,'company_information_html/edit/edit_product.html', {'product': product})  

def destroy_product(request, ProductID):  
    product = Product.objects.get(ProductID=ProductID)
    product.delete()
    return redirect("/company_information/product")  


#-------------------------------------------------------------------------------
def emp_supplier(request):  
    if request.method == "POST":   
        form = SupplierForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/company_information/supplier')      
            except:  
                traceback.print_exc()
    else:  
        form = SupplierForm()  
    return render(request,'company_information_html/index/index_supplier.html',{'form':form})  
   

def supplier(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:
            data_dict["SupplierID__contains"] = search_data    #  搜索  SupplierID 
        suppliers = Supplier.objects.filter(**data_dict).all()

        paginator = Paginator(suppliers,10)
        page = request.GET.get('page1')
        try:
            suppliers = paginator.page(page)               
        except PageNotAnInteger:
            suppliers = paginator.page(1)
        except EmptyPage:
            suppliers = paginator.page(paginator.num_pages)
        context = {'suppliers': suppliers,'search_data':search_data}                          
        return render(request,'company_information_html/list/supplier.html', context)                      

def edit_supplier(request, SupplierID):  
    supplier = Supplier.objects.get(SupplierID=SupplierID)
    return render(request,'company_information_html/edit/edit_supplier.html', {'supplier':supplier,})  

def update_supplier(request, SupplierID):  
    supplier = Supplier.objects.get(SupplierID=SupplierID)
    form = SupplierForm(request.POST, instance = supplier)  
    if form.is_valid():  
        form.save()
        return redirect("/company_information/supplier")  
    return render(request,'company_information_html/edit/edit_supplier.html', {'supplier': supplier})  

def destroy_supplier(request, SupplierID):  
    supplier = Supplier.objects.get(SupplierID=SupplierID)
    supplier.delete()
    return redirect("/company_information/supplier") 

#----------------------------------------------------------------------------

    

  