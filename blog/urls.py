from django.urls import path

from .views import *

app_name='blog'
urlpatterns = [
     
    
    path('/',article_search_view, name='search'),
    path('create/',blog_create_view, name='create'),
    path('<slug:slug>/',blog_detail_view, name='detail'),
    
]
