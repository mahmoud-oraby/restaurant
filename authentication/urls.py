from django.urls import path
from . import views

urlpatterns = [
    path("",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.sign_out,name="logout"),
    path("done/",views.done,name="done"),
]

