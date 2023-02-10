from django.urls import path
from . import views

#esto es para url del normal
urlpatterns = [
    path('',views.index, name='index'),
]