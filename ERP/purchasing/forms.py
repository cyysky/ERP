from django import forms  
from ERPSystem.models import Supplier,Material_Supplier

#----------------------------------------------------------------------------
   
class SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = '__all__'
        
class Material_SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Material_Supplier  
        fields = '__all__'        
