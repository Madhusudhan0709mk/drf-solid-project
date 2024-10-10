# api/urls.py

from django.urls import path
from .views import RecordView



urlpatterns = [
    path('records/', RecordView.as_view()),  
    path('records/<int:record_id>/', RecordView.as_view()),
]


