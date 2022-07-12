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

class Material_Stock01Form(forms.ModelForm):  
    class Meta:  
        model = Material_Stock  
        fields = 'MaterialStockID','material_name','material_location_id','shelf_id','quantity'  
