from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='MarkTime-Index'),
    path('eboard/<str:eboard_first_name>_<str:eboard_last_name>/', views.eboard_member, name='MarkTime-Eboard'),
    path('leadership/', views.leadership, name='MarkTime-Leadership'),
    path('FAQ/',views.faq, name='MarkTime-FAQ'),
    path('songs/', views.songs, name='MarkTime-Songs')
]