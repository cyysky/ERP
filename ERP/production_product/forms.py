
from django import forms  
from ERPSystem.models import BOM,Process,Resource,Machine
from django.db.models import Sum

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
        fields = '__all__' 
    #    fields = 'BOMID','BOM_Level','product_name','material_name','source','UOM','usage','unit_price','remarks','amount','total'
    def save(self, commit=True,):      
        instance = super().save(commit=False)
        # your calculate  
        if instance.total !=0:                 #这有操作问题 需要再次更改 目前功能可用   total= 0 或 total=>1
         instance.amount = instance.usage * instance.unit_price
        else:
          TestID=instance.material_name
          instance.unit_price = BOM.objects.filter(product_name=TestID).aggregate(Sum('amount')).get('amount__sum') or 0.0
          instance.amount = instance.usage * instance.unit_price
        if commit:
           instance.save()
        return instance
      
    def __init__(self, *args, **kwargs): 
        super(BOM01Form, self).__init__(*args, **kwargs)       
        self.fields['ProductID'].disabled = True
        self.fields['MaterialID'].disabled = True

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
        instance.cost = instance.quanitiy * instance.unit_price       #cost 等于 quanitiy 乘 unit_price
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





      

