from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.models import Account
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def registration(request):
    if 'email' in request.POST and request.POST['email'] != '':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        if Account.objects.filter(email=email).first():
            messages.error(request, 'This email already in use')
            return redirect('/auth/registration')
        else:
            user = Account.objects.create_user(email, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            messages.success(request, 'Login now')
            return redirect('/auth/login')

    return render(request, 'registration.html')


@csrf_exempt
def login_user(request):
    if 'username' in request.POST and request.POST['username'] != '' and request.POST['password'] != '':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(email=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Your welcome')
                return redirect('/mail/send')
        else:
            messages.error(request, 'You are not registred, please registred now')
            return redirect('/auth/registration')
    return render(request, 'login.html')


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('/auth/login')
