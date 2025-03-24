from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<str:flower_name>/', views.flower_page, name='flower_page'),
]
