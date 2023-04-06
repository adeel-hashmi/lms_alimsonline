from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


# Create your views here.
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# def home(request):
#     return HttpResponse("Home page ")


def home(request):
    return render(request, 'user_auth/index.html')


def student_signup(request):
    return render(request, 'user_auth/student-signup.html')


def teacher_signup(request):
    return render(request, 'user_auth/teacher-signup.html')


def signin(request):
    return render(request, 'user_auth/signin.html')


def signout(request):
    pass