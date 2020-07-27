from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def login(request):
    return render(request,'login.html')

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    #user exists
    if user is not None:

        return render(request, 'loginsuccessful.html')




    #user not exists
    if user is None:
        return redirect('login')
