from django import forms  
from ERPSystem.models import Supplier,Material_Supplier,Purchase,Require,Receive

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
        fields = 'PurchaseID','purchase_name','deliver_date','material_name','quantity','unit_price','discount','total_MYR','remarks','MaterialSupplierID'


class RequireForm(forms.ModelForm):
    class Meta:
        model = Require
        fields = '__all__'

class Require01Form(forms.ModelForm):
    class Meta:
        model = Require
        fields = 'RequireID','material_name','project_name','material_supplier_name','quantity'


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Receive
        fields = '__all__'
