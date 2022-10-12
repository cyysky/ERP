
from django import forms  
from ERPSystem.models import Sales_Order
#----------------------------------------------------------------------------
class Sales_OrderForm(forms.ModelForm):  
    class Meta:  
        model = Sales_Order  
        fields = '__all__' 

class Sales_Order01Form(forms.ModelForm):  
    class Meta:  
        model = Sales_Order  
        fields = 'SalesOrderID','customer_name','term','customer_po_id','description','quantity','unit_price','start_time','finish_time'
                       

        




      

