from django.shortcuts import render, redirect  
from Master.forms import Sub_contractForm,SupplierForm,CustomerForm,MaterialForm
from Master.models import Sub_contract,Supplier,Customer,Material 
# Create your views here.  
import traceback
def emp(request):  
    if request.method == "POST":  
        form = Sub_contractForm(request.POST)  
        #print(form)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/sub_contract')  
            except:  
                traceback.print_exc()
        else:
            print("invalid ")
    else:  
        form = Sub_contractForm()  
    return render(request,'index.html',{'form':form})  
def sub_contract(request):  
    sub_contracts = Sub_contract.objects.all()  
    return render(request,"sub_contract.html",{'sub_contracts':sub_contracts})  
def edit(request, id):  
    sub_contract = Sub_contract.objects.get(id=id)  
    return render(request,'edit.html', {'sub_contract':sub_contract})  
def update(request, id):  
    sub_contract = Sub_contract.objects.get(id=id)  
    form = Sub_contractForm(request.POST, instance = sub_contract)  
    if form.is_valid():  
        form.save()  
        return redirect("/sub_contract")  
    return render(request, 'edit.html', {'sub_contract': sub_contract})  
def destroy(request, id):  
    sub_contract = Sub_contract.objects.get(id=id)  
    sub_contract.delete()  
    return redirect("/sub_contract") 

def emp1(request):  
    if request.method == "POST":  
        form = SupplierForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/supplier')  
            except:  
                pass  
    else:  
        form = SupplierForm()  
    return render(request,'index1.html',{'form':form})  
def supplier(request):  
    suppliers = Supplier.objects.all()  
    return render(request,"supplier.html",{'suppliers':suppliers})
def edit1(request, id):  
    supplier = Supplier.objects.get(id=id)  
    return render(request,'edit1.html', {'supplier':supplier})  
def update1(request, id):  
    supplier = Supplier.objects.get(id=id)  
    form = SupplierForm(request.POST, instance = supplier)  
    if form.is_valid():  
        form.save()  
        return redirect("/supplier")  
    return render(request, 'edit1.html', {'supplier': supplier})  
def destroy1(request, id):  
    supplier = Supplier.objects.get(id=id)  
    supplier.delete()  
    return redirect("/supplier")     
 
 
def emp2(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/customer')  
            except:  
                pass  
    else:  
        form = CustomerForm()  
    return render(request,'index2.html',{'form':form})  
def customer(request):  
    customers = Customer.objects.all()  
    return render(request,"customer.html",{'customers':customers})  
def edit2(request, id):  
    customer = Customer.objects.get(id=id)  
    return render(request,'edit2.html', {'customer':customer})  
def update2(request, id):  
    customer = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()  
        return redirect("/customer")  
    return render(request, 'edit2.html', {'customer': customer})  
def destroy2(request, id):  
    customer = Customer.objects.get(id=id)  
    customer.delete()  
    return redirect("/customer")

def emp3(request):  
    if request.method == "POST":  
        form = MaterialForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/material')  
            except:  
                pass  
    else:  
        form = MaterialForm()  
    return render(request,'index3.html',{'form':form})  
def material(request):  
    materials = Material.objects.all()  
    return render(request,"material.html",{'materials':materials})  
def edit3(request, id):  
    material = Material.objects.get(id=id)  
    return render(request,'edit3.html', {'material':material})  
def update3(request, id):  
    material = Material.objects.get(id=id)  
    form = MaterialForm(request.POST, instance = material)  
    if form.is_valid():  
        form.save()  
        return redirect("/material")  
    return render(request, 'edit3.html', {'material': material})  
def destroy3(request, id):  
    material = Material.objects.get(id=id)  
    material.delete()  
    return redirect("/material")     