from django import forms  

from employee.models import History

     
#--------------------------------------------------------------------------------------
class HistoryForm(forms.ModelForm):  
    class Meta:  
        model = History  
        fields = "__all__"                          

#------------------------------------------------------------------------------------        
