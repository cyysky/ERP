from lib2to3.pytree import Node
import traceback
from django.shortcuts import render, redirect

from calculator.forms import CalculatorForm,CalculateForm

from calculator.models import Calculator,Calculate

from django.db.models import Sum

from django.db.models import F

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


#---------------------------------------------------------------暂时保留
def compare(request):
    product_ids = request.GET.get('product_ids')
    products = Product.objects.filter(id__in=product_ids)
    return render(request, 'compare.html', {'products': products})

def form_add(request):
    context ={}
  
    # create object of form
    form = AccountForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        form = Calculator.objects.get(name='a')
        form.stories_filed = F('b') + 1
        # save the form data to model
        form.save()
  
    #conte ['form']= form
    return render(request, "add.html", context)
#------------------------------------------------------------

#----------------------------------------------------------
def emp_calculator(request):  
    if request.method == "POST":   
        form = CalculatorForm(request.POST) 
        calculate = Calculate.objects.all()
        calculate.delete()  
        if form.is_valid():
            try:            
                form.save()
                Calculate.objects.create(calculate01='0',calculate02='0',calculate03='0',calculate04='0')
                return redirect('/calculator/calculator')      
            except:  
                traceback.print_exc()
    else:  
        form = CalculatorForm()
    return render(request,'index/index_calculator.html',{'form':form})  
     
def calculator(request):#查询所有数据的数量
        #a=Calculate.objects.all().count()
        #input(a)
        #if a.is_valid(0):
        #Calculate.objects.create(calculate01='0',calculate02='0',calculate03='0') 
        calculators = Calculator.objects.all()
        M=Calculator.objects.all().aggregate(Sum('a')).get('a__sum')
        print('material=',M)   
        M1=Calculator.objects.all().aggregate(Sum('b')).get('b__sum')
        print('material single cost=',M1)   
        B=Calculator.objects.all().aggregate(Sum('c')).get('c__sum')
        print('BOM',B)
        B1=Calculator.objects.all().aggregate(Sum('d')).get('d__sum')
        print('BOM single cost=',B1)
        #def calculator(request):
        #calculate.delete()
        P = lambda M,M1,B,B1: M*M1 + B*B1
        P1 =(P(M,M1,B,B1))
        print(P1)   
        Calculate.objects.update(calculate01=M,calculate02=M1,calculate03=B,calculate04=B1,calculate05=P1)         
       
        paginator = Paginator(calculators,10)
        page = request.GET.get('page1')
        try:
            calculators = paginator.page(page)               
        except PageNotAnInteger:
            calculators = paginator.page(1)
        except EmptyPage:
            calculators = paginator.page(paginator.num_pages)
        
        calculates = Calculate.objects.all()
        paginator = Paginator(calculates, 10)
        page = request.GET.get('page2')
        try:
            calculates = paginator.page(page)             #### 第2分页 功能暂时保存   
        except PageNotAnInteger:
            calculates = paginator.page(1)
        except EmptyPage:
            calculates = paginator.page(paginator.num_pages)

        context = {'calculators': calculators,'calculates':calculates}                
        return render(request,'list/calculator.html', context)                      
         
def edit_calculator(request, id):  
    calculator = Calculator.objects.get(id=id)
    return render(request,'edit/edit_calculator.html', {'calculator':calculator,})  

def update_calculator(request, id):  
    calculator = Calculator.objects.get(id=id)
    form = CalculatorForm(request.POST, instance = calculator)  
    if form.is_valid():  
        form.save()
        return redirect("/calculator/calculator")  
    return render(request,'edit/edit_calculator.html', {'calculator': calculator})  

def destroy_calculator(request, id):  
    calculator = Calculator.objects.get(id=id)
    calculator.delete()
    return redirect("/calculator/calculator") 

def destroy_calculate(request, id):  
    calculate = Calculate.objects.get(id=id)
    calculate.delete()
    return redirect("/calculator/calculator") 
#-------------------------------------------------------------------------------------

    #a=Statistics.objects.all().count() #查询所有数据的数量
    #print(a) 



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
