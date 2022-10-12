
from django import forms  
from ERPSystem.models import Employee,Customer,Product,Supplier

#--------------------------------------------------------------------------------------------
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = '__all__'   

class Employee01Form(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = 'EmployeeID','employee_name','ICor_Passport_No','moblie_contact','email','date_birth','date_join','hour_rate_RM','month_rate_RM','position','level','department','date_left'   

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer          
        fields = '__all__'

class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = '__all__'

class Product01Form(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = 'ProductID','product_name','product_group','product_tooling','product_unit','BOM_Level','quantity','product_type','unit_price','start_time','finish_time'  
class SupplierForm(forms.ModelForm):  
    class Meta:  
        model = Supplier  
        fields = '__all__'