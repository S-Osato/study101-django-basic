from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.helloworldfunction),
    path('create/', views.CharactorCreate.as_view(), name='create'),
    path('list/', views.CharactorList.as_view(), name='list'),
]
