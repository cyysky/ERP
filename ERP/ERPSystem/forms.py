from django import forms  
#from django.db import models 
from ERPSystem.models import History
from ERPSystem.models import Employee
from ERPSystem.models import Product_Quotation,Product_Quotation_Process,Product_Quotation_Material,Product_Quotation_Grand_Total

     
#--------------------------------------------------------------------------------------
class HistoryForm(forms.ModelForm):  
    class Meta:  
        model = History  
        fields = "__all__"                          

#------------------------------------------------------------------------------------        
class Product_QuotationForm(forms.ModelForm):  
    class Meta:  
        model = Product_Quotation 
        fields = "__all__"

class Product_Quotation_ProcessForm(forms.ModelForm):  
    class Meta:  
        model = Product_Quotation_Process 
        fields = "__all__"

class Product_Quotation_MaterialForm(forms.ModelForm):  
    class Meta:  
        model = Product_Quotation_Material 
        fields = "__all__"

class Product_Quotation_Grand_TotalForm(forms.ModelForm):  
    class Meta:  
        model = Product_Quotation_Grand_Total 
        fields = "__all__"
#--------------------------------------------------------------------------------------------
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"                          


#----------------------------------------------------测试(form)自定义
#  {{ form.name }} 普通 input
#
#class UserModelForm(forms.ModelForm):
#    class meta:
#        model = models.UsertInfo
#        fields ={'name','password',}
#        widgets = {
#            'name': forms.TextInput(attrs={'class':'form-control'}),
#            'password': forms.PasswordInput(attrs={'class':'form-control'}),
#            'age': forms.TextInput(attrs={'class':'form-control'}),
#            }