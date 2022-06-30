from django.db import models

class Calculator(models.Model):
    name = models.CharField(max_length=100) 
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)    
    class Meta:  
        db_table = "calculator"
        
class Calculate(models.Model):
    calculate01 = models.CharField(max_length=100)
    calculate02 = models.CharField(max_length=100)
    calculate03 = models.CharField(max_length=100)
    class Meta:  
        db_table = "calculate"
                
        