from django import forms  
from ERPSystem.models import Sales,Customer,Project,BOM,Supplier

#----------------------------------------------------------------------------
class SalesForm(forms.ModelForm):  
    class Meta:  
        model = Sales  
        fields = '__all__'     

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer          
        fields = '__all__'
        
class SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = '__all__'                       
#---------------------------------------------------------------------------
class ProjectForm(forms.ModelForm):  
    class Meta:  
        model = Project  
        fields = '__all__'   

#-------------------------------------------------------------------------------
class BOMForm(forms.ModelForm):  
    class Meta:  
        model = BOM  
        fields = '__all__'
