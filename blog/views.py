from django.shortcuts import render
from django.views.generic import View
from .models import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


'''
Функция post_detail заменена на класс-наследник PostDetail(View)
View обрабатывает все виды HTTP запросов, а не только GET, как это делала функция post_detail
'''

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     all_tags = post.tags.all()
#     return render(request, 'blog/post_detail.html', context={'post': post, 'all_tags': all_tags})


class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        all_tags = post.tags.all()
        return render(request, 'blog/post_detail.html', context={'post': post, 'all_tags': all_tags})





def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    all_posts_from_tag = tag.posts.all()
    return render(request, 'blog/tag_detail.html', context={'tag': tag, 'all_posts': all_posts_from_tag})
