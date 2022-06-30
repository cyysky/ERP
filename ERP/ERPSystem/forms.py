from django import forms  

from ERPSystem.models import History

     
#--------------------------------------------------------------------------------------
class HistoryForm(forms.ModelForm):  
    class Meta:  
        model = History  
        fields = "__all__"                          

#------------------------------------------------------------------------------------        
