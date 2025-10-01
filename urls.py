# student_chatbot/urls.py
# student_chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('chatbot/', views.chatbot_home, name='chatbot_home'),
    path('chatbot/api/', views.chatbot_api, name='chatbot_api'),
]