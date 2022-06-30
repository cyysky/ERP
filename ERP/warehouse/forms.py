from django import forms  

from ERPSystem.models import Material,Material_Location


#--------------------------------------------------------------------------------材料        
class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = '__all__'      

class Material_LocationForm(forms.ModelForm):  
    class Meta:  
        model = Material_Location  
        fields = '__all__'      
        
