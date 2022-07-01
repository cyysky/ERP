from django import forms  
from ERPSystem.models import Supplier,Material_Supplier,Purchase

#----------------------------------------------------------------------------
   
class SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = '__all__'
        
class Material_SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Material_Supplier  
        fields = '__all__'    
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

