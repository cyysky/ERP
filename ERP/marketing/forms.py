from tkinter import NO
from django import forms  
from ERPSystem.models import Sales,Customer,Project,BOM
from django.db.models import Sum
#----------------------------------------------------------------------------
class SalesForm(forms.ModelForm):  
    class Meta:  
        model = Sales  
        fields = '__all__' 

class Sales01Form(forms.ModelForm):  
    class Meta:  
        model = Sales  
        fields = 'SalesID','customer_name','term','customer_po_id','description','quantity','unit_price','start_time','finish_time'
                       
class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer          
        fields = '__all__'

 #---------------------------------------------------------------------------
class ProjectForm(forms.ModelForm):  
    class Meta:  
        model = Project  
        fields = '__all__'    

class Project01Form(forms.ModelForm):  
    class Meta:  
        model = Project   
        fields = 'ProjectID','project_name','customerpart_id','product_name','quantity','unitprice','project_date','term','start_time','finish_time','DeliveryDatetime'

#-------------------------------------------------------------------------------
class BOMForm(forms.ModelForm):  
    class Meta:  
        model = BOM  
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        # your calculate
        instance.amount = instance.usage * instance.unit_price 
        if commit:
            instance.save()
        return instance    

class BOM01Form(forms.ModelForm):  
    class Meta:  
        model = BOM  
        fields = 'BOMID','BOM_Level','ProductID','product_name','MaterialID','material_name','source','UOM','usage','unit_price','remarks','amount','total'
    def save(self, commit=True):
        instance = super().save(commit=False)
        TestID=instance.MaterialID
        # your calculate  
        if instance.unit_price !=0:
         instance.amount = instance.usage * instance.unit_price
        else:      
          instance.unit_price = BOM.objects.filter(ProductID=TestID).aggregate(Sum('amount')).get('amount__sum') or 0.0
          instance.amount = instance.usage * instance.unit_price 
          print(instance.unit_price )    
          print(TestID)
        if commit:
           instance.save()
        return instance    
      