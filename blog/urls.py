from django.urls import path
from .views import *

"""
path(...) является URL шаблоном. name - имя URL шаблона, используется в функции get_absolute_url в post.models
"""
urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/<str:slug>/', tag_detail, name='tag_detail_url'),
]
