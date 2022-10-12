from django import forms
from django.db.models import F, Sum, Window,Avg,OuterRef,Subquery
from ERPSystem.models import Supplier,Material_Supplier,Purchase,Require,Material_Receive

#----------------------------------------------------------------------------
   
class SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = '__all__'

class Material_SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Material_Supplier  
        fields = '__all__'
        
class Material_Supplier01Form(forms.ModelForm):  
    class Meta:  
        model = Material_Supplier  
        fields = 'MaterialSupplierID','material_name','source','UOM','EOQ','unit_price','term','remarks'    
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class Purchase01Form(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = 'PurchaseID','purchase_name','deliver_date','material_name','quantity','unit_price','discount','total_MYR','remarks'
    def save(self, commit=True):
        instance = super().save(commit=False)
        # your calculate       instance.QTY_purchase = instance.QTY_need - instance.QTY_stock
        instance.total_MYR=instance.quantity * instance.unit_price
        if commit:
            instance.save()
        return instance 

class RequireForm(forms.ModelForm):
    class Meta:
        model = Require
        fields = '__all__'
class Require01Form(forms.ModelForm):
    class Meta:
        model = Require
        fields = 'RequireID','project_name','product_name','material_name','product_usage','QTY_project','QTY_need','QTY_stock','QTY_purchase','remarks','quantity'
    def save(self, commit=True):
        instance = super().save(commit=False)
        # your calculate
        if instance.quantity[0]:            #  可用需要改良使用方式    现在是以 更改html update 使用
          TestID=instance.product_name
          instance.QTY_project = Require.objects.filter(material_name=TestID).aggregate(Sum('QTY_purchase')).get('QTY_purchase__sum') or  instance.QTY_project
          instance.QTY_need = instance.product_usage * instance.QTY_project
          instance.QTY_purchase = instance.QTY_need - instance.QTY_stock
        else:
          instance.QTY_need = instance.product_usage * instance.QTY_project
          instance.QTY_purchase = instance.QTY_need - instance.QTY_stock
        if commit:
            instance.save()
        return instance    

class Material_ReceiveForm(forms.ModelForm):
    class Meta:
        model = Material_Receive
        fields = '__all__'