from django.shortcuts import render, redirect
import traceback

from .forms import BOMForm,ProcessForm,ResourceForm,MachineForm
from .forms import BOM01Form,Process01Form

from ERPSystem.models import BOM,Process,Resource,Machine
from ERPSystem.models import Require,Product
#----------------------------------------------------------------------------------------------
from django.db.models import Sum,F,Window 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
#--------------------------------------------------------------------------------
def multi_table_view_production_product(request):
  boms = BOM.objects.all()
  processs = Process.objects.all()
  resources  = Resource.objects.all()
  machines = Machine.objects.all()
  context ={'boms': boms, 
            'processs': processs,
            'resources': resources,
            'machines': machines,}
  return render(request,'production_product_html/multi_table_view_production_product.html', context)   
#-------------------------------------------------------------------------------
def emp_bom(request):  
    if request.method == "POST":   
        form = BOMForm(request.POST)        
        if form.is_valid():  
            try: 
                form.save()                

                return redirect('/production_product/bom')      
            except:  
                traceback.print_exc()
 
    else:                

        form = BOMForm()  
    return render(request,'production_product_html/index/index_bom.html',{'form':form})  
 
def bom(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                #搜索功能 和在  bom.html  request.GET.get('search',"") 对应  <input type="text" name="search"
        if search_data:
            data_dict["BOMID__contains"] = search_data    #  搜索  BOMID 
        boms = BOM.objects.filter(**data_dict).values('BOMID',
                                                      'BOM_Level',
                                                      'ProductID',
                                                      'MaterialID',
                                                      'source',
                                                      'UOM',
                                                      'usage',
                                                      'unit_price',
                                                      'remarks',
                                                      'amount',)

        products = Product.objects.all()
        print(products)
        
        BOM.objects.values('ProductID').update(product_name=(F('ProductID')))
        BOM.objects.values('MaterialID').update(material_name=(F('MaterialID')))
        paginator = Paginator(boms,1)
        page = request.GET.get('page1')
        try:
            boms = paginator.page(page)               
        except PageNotAnInteger:
            boms = paginator.page(1)
        except EmptyPage:
            boms = paginator.page(paginator.num_pages)
        context = {'boms': boms,'search_data':search_data}                          
        return render(request,'production_product_html/list/bom.html', context)                      
     
def edit_bom(request, BOMID):
    bom = BOM.objects.get(BOMID=BOMID)      
    Require.objects.filter(BOMID=BOMID).update(
                           ProductID=bom.ProductID,
                           product_name=bom.product_name,
                           MaterialID=bom.MaterialID,
                           material_name=bom.material_name
                           )  
    return render(request,'production_product_html/edit/edit_bom.html', {'bom':bom,})  

def update_bom(request, BOMID):  
    bom = BOM.objects.get(BOMID=BOMID)
    form = BOM01Form(request.POST, instance = bom)  
    if form.is_valid():  
        form.save()
    return render(request,'production_product_html/edit/edit_bom.html', {'bom': bom})

def destroy_bom(request, BOMID):  
    bom = BOM.objects.get(BOMID=BOMID) 
    bom.delete()
    return redirect("/production_product/bom")  

def update_bom_to_require(request, BOMID):
   if request.method == "GET":
    bom = BOM.objects.get(BOMID=BOMID)
    if Require.objects.filter(BOMID=BOMID) :
     Require.objects.filter(BOMID=BOMID).update(
                            ProductID=bom.ProductID,
                           product_name=bom.product_name,
                           MaterialID=bom.MaterialID,
                           material_name=bom.material_name
                           ) 
     return redirect("/purchasing_material/require")
    else:                
     return redirect("/production_product/bom")  
#-------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------

def emp_process(request):  
    if request.method == "POST":   
        form = ProcessForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production_product/process')      
            except:  
                traceback.print_exc()
    else:  
        form = ProcessForm()  
    return render(request,'production_product_html/index/index_process.html',{'form':form})  
 




def process(request):
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["ProcessID__contains"] = search_data #  搜索  ProcessID  
        processs= Process.objects.filter(**data_dict).values('ProcessID',
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
                                         ).annotate(total=Window(Sum('cost'),order_by=F('ProcessID').asc())) #,order_by=('ProcessID','ProductID')))
        if Process.objects.values('ProjectSalesItemID'):
            Process.objects.values('ProjectSalesItemID').update(project_name=(F('ProjectSalesItemID')))

        paginator = Paginator(processs,10)
        page = request.GET.get('page1')
        try:
            processs = paginator.page(page)               
        except PageNotAnInteger:
            processs = paginator.page(1)
        except EmptyPage:
            processs = paginator.page(paginator.num_pages)
        context = {'processs': processs,'search_data':search_data}                 
        return render(request,'production_product_html/list/process.html', context)                      

def edit_process(request, ProcessID):  
    process = Process.objects.get(ProcessID=ProcessID)
    return render(request,'production_product_html/edit/edit_process.html', {'process':process,})  

def update_process(request, ProcessID):  
    process = Process.objects.get(ProcessID=ProcessID)
    form = Process01Form(request.POST, instance = process)  
    if form.is_valid():  
        form.save()
        return redirect("/production_product/process")  
    return render(request,'production_product_html/edit/edit_process.html', {'process': process})  

def destroy_process(request, ProcessID):  
    process = Process.objects.get(ProcessID=ProcessID)
    process.delete()
    return redirect("/production_product/process")  
#-----------------------------------------------------------------------------------------------------------------------------------------

def emp_resource(request):  
    if request.method == "POST":   
        form = ResourceForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()               
                return redirect('/production_product/resource')      
            except:  
                traceback.print_exc()
    else:  
        form = ResourceForm()  
    return render(request,'production_product_html/index/index_resource.html',{'form':form})  
  
def resource(request):    
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["ResourceID__contains"] = search_data #  搜索  ResourceID  
        resources = Resource.objects.filter(**data_dict).all()
        paginator = Paginator(resources,10)
        page = request.GET.get('page1')
        try:
            resources = paginator.page(page)               
        except PageNotAnInteger:
            resources = paginator.page(1)
        except EmptyPage:
            resources = paginator.page(paginator.num_pages)
        context = {'resources': resources,'search_data':search_data}                          
        return render(request,'production_product_html/list/resource.html', context)                      

def edit_resource(request, ResourceID):  
    resource = Resource.objects.get(ResourceID=ResourceID)
    return render(request,'production_product_html/edit/edit_resource.html', {'resource':resource,})  

def update_resource(request, ResourceID):  
    resource = Resource.objects.get(ResourceID=ResourceID)
    form = ResourceForm(request.POST, instance = resource)  
    if form.is_valid():  
        form.save()
        return redirect("/production_product/resource")  
    return render(request,'production_product_html/edit/edit_resource.html', {'resource': resource})  

def destroy_resource(request, ResourceID):  
    resource = Resource.objects.get(ResourceID=ResourceID)
    resource.delete()
    return redirect("/production_product/resource")    

#------------------------------------------------------------------------------------------------
def emp_machine(request):  
    if request.method == "POST":   
        form = MachineForm(request.POST)        
      
        if form.is_valid():  
            try: 
                form.save()
                
                return redirect('/production_product/machine')      
            except:  
                traceback.print_exc()
    else:  
        form = MachineForm()  
    return render(request,'production_product_html/index/index_machine.html',{'form':form})  
   
def machine(request):  
        data_dict = {}   # 清空
        search_data = request.GET.get('search',"")                
        if search_data:  # 用定义  models.objects.filter(**data_dict).all     显示数据  ,'search_data':search_data
            data_dict["MachineID__contains"] = search_data #  搜索  MachineID  
        machines = Machine.objects.filter(**data_dict).all() 
        paginator = Paginator(machines,10)
        page = request.GET.get('page1')
        try:
            machines = paginator.page(page)               
        except PageNotAnInteger:
            machines = paginator.page(1)
        except EmptyPage:
            machines = paginator.page(paginator.num_pages)
        context = {'machines': machines,'search_data':search_data}                          
        return render(request,'production_product_html/list/machine.html', context)                      

def edit_machine(request, MachineID):  
    machine = Machine.objects.get(MachineID=MachineID)
    return render(request,'production_product_html/edit/edit_machine.html', {'machine':machine,})  

def update_machine(request, MachineID):  
    machine = Machine.objects.get(MachineID=MachineID)
    form = MachineForm(request.POST, instance = machine)  
    if form.is_valid():  
        form.save()
        return redirect("/production_product/machine")  
    return render(request,'production_product_html/edit/edit_machine.html', {'machine': machine})  

def destroy_machine(request, MachineID):  
    machine = Machine.objects.get(MachineID=MachineID)
    machine.delete()
    return redirect("/production_product/machine")
  