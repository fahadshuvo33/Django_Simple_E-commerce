from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("registration/", views.registrationPage, name="register"),
    path('logout/',views.logout_Page,name='logout'),
]