from functools import total_ordering
from django import forms  
from django.db.models import F, Sum, Window,Avg,OuterRef,Subquery
from ERPSystem.models import Process,Resource,Machine,Product
from ERPSystem.models import Product_Good,Product_Reject,Product_Material
from ERPSystem.models import Packaging,Delivery


#---------------------------------------------------------------------Process
class ProcessForm(forms.ModelForm):  
    class Meta:
        model = Process
    #    ordering = ['ProductID', 'ProcessID']
        fields = '__all__'      
    def save(self, commit=True):
        instance = super().save(commit=False)
        # your calculate
        instance.cost = instance.quanitiy * instance.unit_price 
        if commit:
            instance.save()
        return instance    
    
class Process01Form(forms.ModelForm):  
    class Meta:       
        model = Process  
        fields = 'ProcessID','process_name','process_tooling','duration','quanitiy','unit_price','cost','total'
    def save(self,commit=True):
        instance = super().save(commit=False)
    #    if instance.total !=0:
    #     instance.cost = instance.quanitiy * instance.unit_price 
    #    else:  
    #     instance.cost = instance.quanitiy * instance.unit_price
    #    instance.total=Process.objects.update(total=Subquery(Process.objects.annotate(cumsum=Window(Sum('cost')).values('cumsum'))[:1]))
       # instance.total=Subquery(Process.objects.annotate(cumsum=Window(Sum('cost'))).values('cumsum')[:1])
     #   Process.objects.total=Process.objects.values('ProductID').annotate(cumsum=Window(Sum('cost'))).values('cumsum')[:1]

     #   print(instance.total)
     #    instance.total =Process.objects.values('ProductID').annotate(Sum('total')).update(total=(Process.objects.annotate(cumsum=Window(Sum('cost'))).values('cost')[:1] ) )
     #    instance.total =Process.objects.values('ProcessID').annotate(total =Window(Sum('cost'),order_by=F('ProcessID').asc()))
      #  a= Process.objects.values('cost').annotate(total=Window(Sum('cost'),order_by=F('ProcessID').asc()))
      #  print(a)
      #  b=a.values('total')
      #  c=[b]
      #  print(b)
     #    instance.total = Process.objects.filter(vendor=pk,date__range=(form.cleaned_data['start_date'], 
      #                                                                              form.cleaned_data['end_date'])).order_by('pk').annotate(cumbalance=Window(Sum('balance'), order_by=F('id').asc()))
      #   instance.total= Process.objects.values('total').update(total=c.list('total'))
     #   Process.objects.values('cost').annotate(Z=Sum('cost')).update(total=(Process.objects.annotate(cumsum=Window(Sum('cost'))).values('cumsum')[:1] ) )
        
    #    items = self.client.invoice_set.all()
       #  Process.objects.values('cost').annotate(total=Window(Sum('cost'),order_by=F('ProcessID').asc()))

    #    if instance.total !=0:
    #      instance.total = Process.objects.values('cost').annotate(total=Window(Sum('cost'),order_by=F('ProcessID').asc()))
    #    else: 
    #      instance.total = Process.objects.values('cost').annotate(total=Window(Sum('cost'-'cost'),order_by=F('ProcessID').asc()))

   #     Process.objects.values('ProcessID')(instance.total = ('instance.cost') + ('instance.cost'))

        # **  filter   update
    #    instance.total = Process.objects.all('ProcessID').values('cost').annotate(Sum('cost')).update(total=b)
     #   Process.objects.all().values('cost').update(total=b)
      #  print(instance.total)total.aggregate(Sum('column')).get('column__sum')
      #  instance.total = Process.objects.values('cost').aggregate(Sum('cost')).get('cost__sum')
   #     instance.total = Process.objects.exclude(total=True).values('cost').annotate(total=Sum('cost')).order_by('ProcessID')
      #  Blog.objects.update(rating=Subquery(Blog.objects.filter(id=OuterRef('id')).annotate(avg_rating=Avg('cost')).values('ProcessID')[:1]))
       # Sql =  SELECT *, sum(cost) OVER (ORDER BY ProjectID, ProcessID) AS total FROM Process ORDER BY ProjectID, ProcessID’’’
     #   Process.objects.update(total=Subquery(Process.objects.all().annotate(cumsum=Window(Sum('cost'))).update(total=F('cumsum'))))
    #    Process.objects.all().annotate(cumsum=Window(Sum('cost')).update(total=int('cumsum')))
     #   c= Process.objects.filter(total=b)
     #   instance.total=(c)  
        if commit:
           instance.save()
        return instance    
 
#---------------------------------------------------------------------resource
class ResourceForm(forms.ModelForm):  
    class Meta:  
        model = Resource  
        fields = '__all__'  
                   
#---------------------------------------------------------------------------------机器        
class MachineForm(forms.ModelForm):  
    class Meta:  
        model = Machine  
        fields = '__all__'
#----------------------------------------------------------------------------------产品  
      
class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = '__all__'

class Product01Form(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = 'ProductID','product_name','product_group','product_tooling','product_unit','quantity','product_type','unit_price','start_time','finish_time'  
     
     
class Product_GoodForm(forms.ModelForm):  
    class Meta:  
        model = Product_Good  
        fields = '__all__'   
 
class Product_RejectForm(forms.ModelForm):  
    class Meta:  
        model = Product_Reject  
        fields = '__all__'    

#-------------------------------------------------------------
class Product_Good01Form(forms.ModelForm):  
    class Meta:  
        model = Product_Good  
        fields = 'GoodbatchID','product_name','type','quantity','term'   

class Product_Reject01Form(forms.ModelForm):  
    class Meta:  
        model = Product_Reject  
        fields = 'RejectbatchID','product_name','type','quantity'   

#--------------------------------------------------------------------

class Product_MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Product_Material  
        fields = '__all__'           
       
#---------------------------------------------------------------------------
class PackagingForm(forms.ModelForm):
    class Meta:
        model = Packaging
        fields = '__all__'

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class Delivery01Form(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = 'DeliveryID','sales_name','product_name','quantity','unitprice','term','DeliveryDatetime'