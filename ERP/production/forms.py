from django import forms  

from ERPSystem.models import Process,Machine,Product,Product_Good,Product_Reject,Product_Material,Packaging,Delivery

#---------------------------------------------------------------------
class ProcessForm(forms.ModelForm):  
    class Meta:  
        model = Process  
        fields = '__all__'      
          
#---------------------------------------------------------------------------------机器        
class MachineForm(forms.ModelForm):  
    class Meta:  
        model = Machine  
        fields = '__all__'
#----------------------------------------------------------------------------------产品  
      
class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = '__all__'  
     
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
        fields = 'RejectbatchID','product_name','type','quantity',   

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