from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        UN = request.POST['username']
        PWD = request.POST['password']
        PWD2 = request.POST['cpassword']
        if PWD == PWD2:
            if User.objects.filter(username=UN).exists():
                messages.info(request, "Username already exists.")
                return redirect('creds:register')  # Fixed redirect statement
            else:
                user = User.objects.create_user(username=UN, password=PWD)
                user.save()
                messages.info(request, "User created")
                return redirect("creds:login")
        else:
            messages.info(request, "Passwords do not match")
            return redirect('creds:register')
    return render(request, 'register.html')


def login(request ):
    if request.method == 'POST':
        UNM = request.POST['username']
        PWRD = request.POST['password']
        user = auth.authenticate(username=UNM, password=PWRD)

        if user is not None:
            auth.login(request, user)
            return redirect("Bankapp:tofill")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("creds:login")
    return render(request, "login.html")

def logout(request):
    return render(request,'login.html')