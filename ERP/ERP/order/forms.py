from django import forms  
from employee.models import Customer,Supplier,Sales,Project
from employee.models import BOM,Packaging
from employee.models import Delivery
from employee.models import Machine,Material,Material_Location,Material_Supplier
from employee.models import Process,Product,Product_Good,Product_Material,Product_Reject

#----------------------------------------------------------------------------销售

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
#-----------------------------------------
class Sales_01Form(forms.ModelForm):  
    class Meta:  
        model = Sales  
        fields =['customer_name','term','date','start_time','finish_time',
         'customer_po_id','product_id','description','quantity','unit_price']     

class Customer_01Form(forms.ModelForm):  
    class Meta:  
        model = Customer          
        fields = ['customer_name','address','term',
         'email','phone1','phone2']
 
class Supplier_01Form(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = ['supplier_name','address','term',
         'email','phone1','phone2']
        
#---------------------------------------------------------------------------------机器        
class MachineForm(forms.ModelForm):  
    class Meta:  
        model = Machine  
        fields = '__all__'
#----------------------------------

#--------------------------------------------------------------------------------材料        
class MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Material  
        fields = '__all__'      

class Material_StockForm(forms.ModelForm):  
    class Meta:  
        model = Material_Location  
        fields = '__all__'      
        
class Material_SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Material_Supplier  
        fields = '__all__'        
#-------------------------------           

class Material_Location_01Form(forms.ModelForm):  
    class Meta:  
        model = Material_Location  
        fields = ['material_id','quantity']      
        
class Material_Supplier_01Form(forms.ModelForm):  
    class Meta:  
        model = Material_Supplier  
        fields = '__all__'         
#----------------------------------------------------------------------------------        
class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = '__all__'  

class ProcessForm(forms.ModelForm):  
    class Meta:  
        model = Process  
        fields = '__all__'      
           
class Product_GoodForm(forms.ModelForm):  
    class Meta:  
        model = Product_Good  
        fields = '__all__'   

class Product_MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Product_Material  
        fields = '__all__'           
     
class Product_RejectForm(forms.ModelForm):  
    class Meta:  
        model = Product_Reject  
        fields = '__all__'   
#------------------------         
class Product_01Form(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = '__all__'  
class Process_01Form(forms.ModelForm):  
    class Meta:  
        model = Process  
        fields = '__all__'     

class Product_Material_01Form(forms.ModelForm):  
    class Meta:  
        model = Product_Material  
        fields = ['material_id','usage']    
           
class Product_Good_01Form(forms.ModelForm):  
    class Meta:  
        model = Product_Good  
        fields = ['product_id','product_name','customer_id','type','quantity','term','date','material_id']          
       
class Product_Reject_01Form(forms.ModelForm):  
    class Meta:  
        model = Product_Reject  
        fields = ['product_id','product_name','type','quantity','date','material_id']          
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

class DeliveryForm(forms.ModelForm):
    class Meta:
        madel = Delivery
        fields = '__all__'

class PackagingForm(forms.ModelForm):
    class Meta:
        madel = Packaging
        fields = '__all__'