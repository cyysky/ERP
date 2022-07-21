from email.mime.text import MIMEText
from django.shortcuts import render,redirect
from cartapp import models
from smtplib import SMTP,SMTPAuthenticationEroor,SMTPExcetion
from email.mime.text import MIMEText

message = ''
cartlist = []
customphone = '' 
customaddress = '' 
customemail = '' 

def index(request):
    global cartlist 
    if 'cartlist' in request.session:
        cartlist = request.session['cartlist']
    else:
        cartlist = []
    cartnum = len(cartlist)
    productall = models.ProduvtModel.objects.all()
    return render(request,"index.html",locals())


