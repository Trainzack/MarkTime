from django.urls import path

from . import views
from .views import RecordingListView

urlpatterns = [
    path('', views.index, name='MarkTime-Index'),
    # Keeping this path here as an example of how to do url paths with arguments
    # path('eboard/<str:eboard_first_name>_<str:eboard_last_name>/', views.eboard_member, name='MarkTime-Eboard'),
    path('leadership/', views.leadership, name='MarkTime-Leadership'),
    path('FAQ/', views.faq, name='MarkTime-FAQ'),
    path('music/', RecordingListView.as_view(), name='MarkTime-Music'),
    path('history/', views.history_index, name='MarkTime-HistoryIndex'),
    path('history/<int:queried_year>', views.history_page, name='MarkTime-HistoryPage'),
    path('contact/join_us/', views.contact_us, name='MarkTime-Contact'),
    path('contact/hire_us/', views.hire_us, name='MarkTime-Contact-Performance'),
    path('music/old', views.songs, name='Whatever')
]