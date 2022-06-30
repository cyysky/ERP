from django import forms  

from calculator.models import Calculator,Calculate

class CalculatorForm(forms.ModelForm):  
    class Meta:  
        model = Calculator  
        fields = '__all__'     

class CalculateForm(forms.ModelForm):  
    class Meta:  
        model = Calculate  
        fields = '__all__'         
                             