from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, auth


# Create your views here.
from django.contrib.auth.forms import UserCreationForm


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'registration/register.html', {'form': form})


# def home(request):
#     return HttpResponse("Home page ")


def home(request):
    return render(request, 'user_auth/index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = email  # set username as email
        password = request.POST['password']
        user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request, 'user_auth/register.html')

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


def teacher_signup(request):
    return render(request, 'user_auth/teacher-signup.html')


def signin(request):
    return render(request, 'user_auth/signin.html')


def signout(request):
    pass