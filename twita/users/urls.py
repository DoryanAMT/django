from django.urls import path
from . import views

#esto es para url del normal
urlpatterns = [

    path("signup/", views.SignUp.as_view(), name="signup"),
]