from django.urls import path
from . import views


    #esto es para url del normal
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detalle, name='detalle'),
    ]
