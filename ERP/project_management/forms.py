
from django import forms  
from ERPSystem.models import Project_Sales_Item

 #---------------------------------------------------------------------------
class Product_Sales_ItemForm(forms.ModelForm):  
    class Meta:  
        model = Project_Sales_Item  
        fields = '__all__'    

class Product_Sales_Item01Form(forms.ModelForm):  
    class Meta:  
        model = Project_Sales_Item   
        fields = 'ProjectSalesItemID','project_name','customerpart_id','product_name','quantity','unitprice','project_date','term','start_time','finish_time','DeliveryDatetime'

        




      

