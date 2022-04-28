from django import forms  
from Master.models import Sub_contract,Supplier,Customer,Material  

class Sub_contractForm(forms.ModelForm):  
    class Meta:  
        model = Sub_contract  
        fields = "__all__" 


class SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = "__all__"  


class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer  
        fields = "__all__" 

class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = "__all__"                  