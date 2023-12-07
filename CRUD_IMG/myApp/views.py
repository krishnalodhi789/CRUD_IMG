from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import CustomForm
import os

# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method == "POST":
        form = CustomForm(request.POST,request.FILES)
        if form.is_valid() and request.FILES != 0:
            form.save()
            return redirect("records")          
        
    form = CustomForm()
    return render(request,'registrationPage.html',{"form":form})

def records(request):
    records = CustomUser.objects.all()
    return render(request, "records.html",{"records":records})

def deleteUser(request,id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    return redirect("records")

def editUser(request,id):
    user = CustomUser.objects.get(pk=id)
    path = user.image.path
    if request.method == "POST":
        updatedUser = CustomForm(request.POST, request.FILES, instance=user)
        if updatedUser.is_valid():
            if request.FILES.get("image") is not None :
                os.remove(path)
            updatedUser.save()
        return redirect("records")
    
    pic = user.image
    form = CustomForm(instance=user)
    return render(request, 'editUser.html', {"form":form, 'pic':pic})