from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.home, name="home"),
    # path('reg/', views.reg, name="register"),
    path('studentSignup/', views.student_signup, name="studentSignup"),
    path('teacherSignup/', views.teacher_signup, name="teacherSignup"),
]
