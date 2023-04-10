from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, auth

from django.contrib import messages

# Create your views here.
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'user_auth/index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = email  # set username as email
        password = request.POST['password']

        # Check if username or email already exists
        if User.objects.filter(username=email).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'A user with this email already exists.', extra_tags='danger')
            return render(request, 'user_auth/register.html')

        # Create the new user
        user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
        # user.save()
        messages.success(request, 'Your account has been created! You can now log in.')
        return render(request, 'user_auth/login.html')
        # print("user created")
        # return redirect('/')
    else:
        return render(request, 'user_auth/register.html')

def teacher_reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = email  # set username as email
        password = request.POST['password']
        is_staff = True

        # Check if username or email already exists
        if User.objects.filter(username=email).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'A user with this email already exists.', extra_tags='danger')
            return render(request, 'user_auth/teacher-reg.html')

        # Create the new user
        user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password, is_staff=is_staff)
        # user.save()
        messages.success(request, 'Your account has been created! You can now log in.')
        return render(request, 'user_auth/login.html')
        # print("user created")
        # return redirect('/')
    else:
        return render(request, 'user_auth/teacher-reg.html')



def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = email
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponse("<h1>Login Successful</h1>")
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'user_auth/login.html')
    else:
        return render(request, 'user_auth/login.html')


# def student_signup(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         email = request.POST['email']
#         password = request.POST['password']
#
#         user = User.objects.create_user(first_name=first_name, email=email, password=password)
#         user.save()
#         print("user created")
#         return redirect('/')
#     else:
#         return render(request, 'user_auth/student-signup.html')








def signout(request):
    pass
