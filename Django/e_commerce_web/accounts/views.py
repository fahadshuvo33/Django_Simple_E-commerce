from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def loginPage(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request ,  username = username, password = password)
        if user is not None :
            login(request, user)
            return redirect('home')
        else :
            messages.error(request,'Username or password not match')
    return render(request,'accounts/login.html')


def registrationPage(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2 and password1 is not None:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.error(request , 'Email is already registered')
            else :
                new_user = User.objects.create_user(username,email, password1)
                new_user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
        
    return render(request,'accounts/signup.html')


def logout_Page(request) :
    logout(request)
    return render(request ,'home.html')

