from django import forms  

from ERPSystem.models import Material,Material_Stock


#--------------------------------------------------------------------------------材料        
class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = '__all__'      

class Material_StockForm(forms.ModelForm):  
    class Meta:  
        model = Material_Stock  
        fields = '__all__'      
        
