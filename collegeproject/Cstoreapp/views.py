from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from . models import Department,Courses,Product
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from.forms import Register
# Create your views here.
def dept(request):
    data=Department.objects.all()
    return render(request,'department.html',{'data':data})
def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
             user=form.save()
             auth.login(request,user)
             messages.success(request,"Registration Succesfull.")
             return redirect('Cstoreapp.login')
    form = UserCreationForm()
    return render(request,"register.html",{'r_form':form})

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, f'Welcome {username}.')
                return redirect('Cstoreapp:shop')
            else:
                messages.error(request, "Invalid User")
        else:
            messages.error(request, "Invalid User")
    form=AuthenticationForm()
    return render(request,"login.html",{"l_form":form})

def shop(request):
    return render(request,"shop.html")

def order(request):
    data= Department.objects.all()
    sub=Courses.objects.all()
    Product.objects.all()
    return render(request,"order.html",{'data':data,'sub':sub})

def logout(request):
    return render(request,"department.html")

