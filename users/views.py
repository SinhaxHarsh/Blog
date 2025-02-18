from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def SignUpView(request):
    if request.method=="POST":
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')

        if password!=confirm_password:
            messages.error(request,"Passwords Didn't Match")
            return render(request,'users/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Is Already In Use")
            return render(request,'users/signup.html')

        user= User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('signin')
    return render(request,'users/signup.html')

def SignInView(request):
    if request.method=="POST":
        email= request.POST.get('email')
        password= request.POST.get('password')
        user= authenticate(request,username=email,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,"Wrong Credentials")
            return redirect('signin')
    return render(request,'users/signin.html')

def SignOutView(request):
    print("You Have Been Signed Out")
    logout(request)
    return redirect('index')