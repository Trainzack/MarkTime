from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='MarkTime-Index'),
    path('eboard/<str:eboard_first_name>_<str:eboard_last_name>/', views.eboard_member, name='MarkTime-Eboard'),
    path('leadership/', views.leadership, name='MarkTime-Leadership'),
    path('FAQ/',views.faq, name='MarkTime-FAQ'),
    path('songs/', views.songs, name='MarkTime-Music'),
    path('history/', views.history_index, name='MarkTime-HistoryIndex'),
    path('history/<int:queried_year>', views.history_page, name='MarkTime-HistoryPage'),
    path('contact-us', views.contact_us, name='MarkTime-Contact')
]