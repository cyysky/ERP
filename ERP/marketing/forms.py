from django import forms  
from ERPSystem.models import Sales,Customer,Project,BOM
#----------------------------------------------------------------------------
class SalesForm(forms.ModelForm):  
    class Meta:  
        model = Sales  
        fields = '__all__' 
class Sales01Form(forms.ModelForm):  
    class Meta:  
        model = Sales  
        fields = 'SalesID','customer_name','term','customer_po_id','description','quantity','unit_price','start_time','finish_time'
                       

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer          
        fields = '__all__'

 #---------------------------------------------------------------------------
class ProjectForm(forms.ModelForm):  
    class Meta:  
        model = Project  
        fields = '__all__'    

class Project01Form(forms.ModelForm):  
    class Meta:  
        model = Project   
        fields = 'ProjectID','project_name','SalesID','CustomerID','customerpart_id','ProductID','product_name','quantity','unitprice','project_date','term' 

#-------------------------------------------------------------------------------
class BOMForm(forms.ModelForm):  
    class Meta:  
        model = BOM  
        fields = '__all__'
          