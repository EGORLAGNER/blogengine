from django.urls import path
from .views import *

"""
path(...) является URL шаблоном. name - имя URL шаблона, используется в функции get_absolute_url в post.models
"""
urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post_create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),

    path('tags/', tags_list, name='tags_list_url'),
    path('tags/<str:slug>/', tag_detail, name='tag_detail_url'),
    path('tag_create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
]
