from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('second/', views.second_view, name='second_view'),
    path('blog/', views.blog, name='blog'),
]