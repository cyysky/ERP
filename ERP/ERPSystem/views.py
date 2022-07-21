from django.shortcuts import render,redirect
from django.db.models import Sum  #能从  .objects.all() 拿记录
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

#------------------------------------------------------------------------------
from ERPSystem.forms import HistoryForm
from ERPSystem.models import History
#-----------------------------------------------

from ERPSystem.models import Delivery,Packaging
from ERPSystem.models import Customer,Supplier,Sales,Project,BOM
from ERPSystem.models import Machine,Material,Material_Stock,Material_Supplier,Require
from ERPSystem.models import Process,Product,Product_Good,Product_Material,Product_Reject
#------------------------------------------------保存现在没用的的宣告功能
import time    
from django.http import FileResponse
from django.shortcuts import HttpResponse                  
from django.db.models import F   
#---------------------------------------------------------- 
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
#-------------------------------------------------------------------------------------
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

def main_page(request):
    saless = Sales.objects.all()
    customers = Customer.objects.all()
    suppliers = Supplier.objects.all()

    machines = Machine.objects.all()

    materials = Material.objects.all()
    material_stocks = Material_Stock.objects.all()
    material_suppliers = Material_Supplier.objects.all()

    products = Product.objects.all()
    processs = Process.objects.all()
    product_materials = Product_Material.objects.all()
    product_goods = Product_Good.objects.all()
    product_rejects = Product_Reject.objects.all()

    context = {'saless': saless,'customers': customers,'suppliers':suppliers,'machines':machines,
               'materials':materials,'material_stocks':material_stocks,'material_suppliers':material_suppliers,
                'processs':processs,'products':products,'product_materials':product_materials,'product_goods':product_goods,
                    'product_rejects':product_rejects}
    return render(request,'main_page.html', context)

def REP_mind_map(request):           #这里需要整理
    saless = Sales.objects.all()
    customers = Customer.objects.all()
    projects = Project.objects.all()    
    boms = BOM.objects.all()
    
    
    machines = Machine.objects.all()

    materials = Material.objects.all()
    material_stocks = Material_Stock.objects.all()
    
    suppliers = Supplier.objects.all()
    material_suppliers = Material_Supplier.objects.all()
    require = Require.object.all()
    
    deliverys = Delivery.objects.all()
    packagings = Packaging.object.all()

    products = Product.objects.all()
    processs = Process.objects.all()
    product_materials = Product_Material.objects.all()
    product_goods = Product_Good.objects.all()
    product_rejects = Product_Reject.objects.all()

    context = {'saless': saless,
               'customers': customers,
               'suppliers':suppliers,
               'projects':projects,
               'boms':boms,

               'machines':machines,

               'materials':materials,
               'material_stocks':material_stocks,

               'material_suppliers':material_suppliers,

               'require':require,

               'processs':processs,
               'products':products,
               'product_materials':product_materials,
               'product_goods':product_goods,
               'product_rejects':product_rejects,
    
               'packagings':packagings,

               'projects':projects,
               'deliverys':deliverys
  }
    return render(request,'REP_mind_map.html', context)


#----------------------------------------------(成本运算系统)  cost calculation system

#def cost_calculation_system(request):

#def emp_cost_calculation_system(request):  
#    if request.method == "POST":  
#        form = CostCalculationSystemForm(request.POST)  
#        if form.is_valid():  
#            try:  
#                form.save()  
#                return redirect('/history')  
#            except:  
#                pass  
#    else:  
#        form = CostCalculationSystemForm()  
#    return render(request,'index/index_cost_calculation_system.html',{'form':form})  

#def cost_calculation_system(request):    
#    cost_calculation_systems = CostCalculationSystem.objects.all()
#    paginator = Paginator(historys,10)
#    page = request.GET.get('page1')
#    try:
#        cost_calculation_systems = paginator.page(page)
#    except PageNotAnInteger:
#        cost_calculation_systems = paginator.page(1)
#    except EmptyPage:
#        cost_calculation_systems = paginator.page(paginator.num_pages)
#    context = {'cost_calculation_systems': cost_calculation_systems,}                          
#    return render(request,'list/cost_calculation_system.html', context)
  
#def edit_cost_calculation_system(request, id):  
#    history = CostCalculationSystem.objects.get(id=id)  
#    return render(request,'edit/edit_history.html', {'cost_calculation_system':cost_calculation_system})  
#def update_cost_calculation_system(request, id):  
#    history = CostCalculationSystem.objects.get(id=id)  
#    form = HistoryForm(request.POST, instance = history)  
#    if form.is_valid():  
#        form.save()  
#        return redirect("/cost_calculation_system")  
#    return render(request, 'edit/edit_cost_calculation_system.html', {'cost_calculation_system': cost_calculation_system})  
#def destroy_cost_calculation_system(request, id):  
#    history = CostCalculationSystem.objects.get(id=id)  
#    history.delete()  
#    return redirect("/cost_calculation_system")



#--------------------------------------------------------------------------再测试的功能区

#----比如P1用M1兩件和M2四件原料，M1單價RM3, M2 單價RM5,  產品P1單價便是M1(2X3)+M2(4X5)=26


 #Statistics.objects.all().count() #查询所有数据的数量
 #Calculate.objects.create(calculate01='0',calculate02='0',calculate03='0')
 #calculators = Product.objects.all()

#re1=Product.objects.all().aggregate(Sum('unit_price')).get('unit_price__sum')
#print(re1)   
#re2=BOM.objects.all().aggregate(Sum('usage')).get('usage__sum')
#print(re2)   
#re3=BOM.objects.all().aggregate(Sum('usage')).get('usage__sum')
#print(re3)  

#---------- P1= M1(2)  + M2(4      M1=3  M2=5      
#---------- P1= M1(2X3)+ M2(4X5) =26  
#P1 = lambda M1,M2,: M1*3 + M2*5
#print(P1(re1,re2))



