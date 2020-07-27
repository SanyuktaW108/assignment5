from django.shortcuts import render
from .models import Customer
from django.contrib.auth.models import User
# Create your views here.
def registration(request):
    return render(request,'registration.html')


def savedata(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    phone_no = request.POST['phone_no']

    User.objects.create_user(username=username, password=password).save()
    Customer(username=username, password=password, email=email, phone=phone_no).save()

    return render(request, 'final.html')
