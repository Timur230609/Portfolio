from django.urls import path
from .views import *

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('',home_view,name='home-page'),
    path('send-message/', send_message, name='send_message')
]