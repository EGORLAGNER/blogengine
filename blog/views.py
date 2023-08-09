from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .utils import ObjectDetailMixin
from .forms import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


"""
Функция post_detail заменена на класс-наследник PostDetail(View).
View обрабатывает все виды HTTP запросов, а не только GET, как это делала функция post_detail.

get_object_or_404 добавляет выброс исключения 404, если контент не найден
get_object_or_404 принимает два аргумента: класс модели и условие по которому будет происходить поиск
если модель найдена по заданному условию, то django сможет "отрисовать" страницу, значит ответ будет со статусом 200 ОК
если модель не найдена, то пользователь увидит ответ со статусом 404
"""

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     all_tags = post.tags.all()
#     return render(request, 'blog/post_detail.html', context={'post': post, 'all_tags': all_tags})


# class PostDetail(View):
#     def get(self, request, slug):
#         post = get_object_or_404(Post, slug__iexact=slug)
#         all_tags = post.tags.all()
#         return render(request, 'blog/post_detail.html', context={'post': post, 'all_tags': all_tags})

"""
PostDetail является миксином.
Обработчки tag_detail выполнен функцией как в первых уроках Молчанова.
Я специально не стал переписывать его с использованием класса или миксина, чтобы была наглядная разница в коде.
"""


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagCreate(View):
    def get(self, request):
        """
        При обращении пользователя по URL отображается форма, в которую
        пользователь будет вносить данные.
        """
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    all_posts_from_tag = tag.posts.all()
    return render(request, 'blog/tag_detail.html', context={'tag': tag, 'all_posts': all_posts_from_tag})
