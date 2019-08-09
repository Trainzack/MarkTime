from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eboard/<str:eboard_first_name>_<str:eboard_last_name>/', views.eboard_member, name='MarkTime-Eboard'),
    path('leadership/',views.leadership, name='MarkTime-Leadership')
]