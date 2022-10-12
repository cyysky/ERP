
from django import forms  
from ERPSystem.models import Material,Material_Stock,Material_Receive

#--------------------------------------------------------------------------------材料        
class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = '__all__'      

class Material01Form(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = 'MaterialID','material_name','measure_unit','tybe','Form','thickness','width','length','pltch','default_stock_locatiuon','quantity','unit_price'      
#,'material_supplier_name'

class Material_StockForm(forms.ModelForm):  
    class Meta:  
        model = Material_Stock  
        fields = '__all__'      

class Material_Stock01Form(forms.ModelForm):  
    class Meta:  
        model = Material_Stock  
        fields = 'MaterialStockID','material_name','material_location_id','shelf_id','quantity'  

class Material_ReceiveForm(forms.ModelForm):
    class Meta:
        model = Material_Receive
        fields = '__all__'