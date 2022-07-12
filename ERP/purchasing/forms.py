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
        fields = 'MaterialSupplierID','material_name','quantity','remarks'    
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class RequireForm(forms.ModelForm):
    class Meta:
        model = Require
        fields = '__all__'

class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Receive
        fields = '__all__'
