from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.home, name='home'),
    path('user_auth/register/', views.register, name="register"),
    path('user_auth/teacher-reg/', views.teacher_reg, name='teacherReg'),
    path('user_auth/signin/', views.signin, name="signin"),
    # path('studentSignup/', views.student_signup, name="studentSignup"),
]
