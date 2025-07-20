from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('', views.admission_view, name='admission'),
    path("login/", views.student_login, name="student_login"),
    path("student/", views.student_page, name="student_page"),
    path("forget-password/", views.forget_password, name="forget_password"),
]