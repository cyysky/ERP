
from django import forms  
from ERPSystem.models import Product_Good,Product_Reject,Product_Material
from ERPSystem.models import Packaging,Delivery


#---------------------------------------------------------------------
    
class Product_GoodForm(forms.ModelForm):  
    class Meta:  
        model = Product_Good  
        fields = '__all__'   
 
class Product_RejectForm(forms.ModelForm):  
    class Meta:  
        model = Product_Reject  
        fields = '__all__'    

#-------------------------------------------------------------
class Product_Good01Form(forms.ModelForm):  
    class Meta:  
        model = Product_Good  
        fields = 'GoodbatchID','product_name','type','quantity','term'   

class Product_Reject01Form(forms.ModelForm):  
    class Meta:  
        model = Product_Reject  
        fields = 'RejectbatchID','product_name','type','quantity'   

#--------------------------------------------------------------------

class Product_MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Product_Material  
        fields = '__all__'           
       
#---------------------------------------------------------------------------
class PackagingForm(forms.ModelForm):
    class Meta:
        model = Packaging
        fields = '__all__'

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class Delivery01Form(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = 'DeliveryID','sales_name','product_name','quantity','unitprice','term','DeliveryDatetime'