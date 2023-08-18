from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .forms import *

# from .utils import ObjectDetailMixin

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

# class PostDetail(ObjectDetailMixin, View):
#     model = Post
#     template = 'blog/post_detail.html'


"""CREATE"""


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            saved_post = request.POST['title']
            return render(request, 'blog/post_create_confirm.html', context={'post': saved_post})
        return render(request, 'blog/post_create.html', context={'form': bound_form})


class TagCreate(View):
    """Создание тегов"""

    def get(self, request):
        """Показывает пустую форму"""
        form = TagForm()
        template = 'blog/tag_create.html'
        context = {'form': form}
        return render(request, template, context)

    def post(self, request):
        """Принимает введенные пользователем данные, проверяет валидность данных:
            если данные валидны, то сохраняет их в базу и показывает страницу с подтверждением;
            если данные не валидны, то показывает туже самую страницу с формой, что и в GET запросе"""
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            saved_tag = request.POST['title']
            return render(request, 'blog/tag_create_confirm.html', context={'tag': saved_tag})
        return render(request, 'blog/tag_create.html', context={'form': form})


"""READ"""


class PostDetail(View):
    """Показывает пост и его теги или если пост не найден - страницу с 404"""

    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        all_tags = post.tags.all()
        return render(request, 'blog/post_detail.html', context={'post': post, 'all_tags': all_tags})


def tag_detail(request, slug):
    """Показывает все посты связанные с тегом"""
    tag = Tag.objects.get(slug__iexact=slug)
    all_posts_from_tag = tag.posts.all()
    return render(request, 'blog/tag_detail.html', context={'tag': tag, 'all_posts': all_posts_from_tag})


def posts_list(request):
    """Показывает все посты"""
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    """Показывает все теги"""
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


"""UPDATE"""


class TagUpdate(View):
    """Изменяет тег"""

    def get(self, request, slug):
        """Показывает форму с заполненными полями"""
        tag = Tag.objects.get(slug__exact=slug)
        form = TagForm(instance=tag)
        return render(request, 'blog/tag_update_form.html', context={'form': form, 'tag': tag})

    def post(self, request, slug):
        """Принимает введенные пользователем данные, проверяет валидность данных:
                    если данные валидны, то сохраняет их в базу и показывает страницу с подтверждением;
                    если данные не валидны, то показывает туже самую страницу с формой, что и в GET запросе"""
        tag = Tag.objects.get(slug__iexact=slug)
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            new_tag = form.save()
            return render(request, 'blog/tag_create_confirm.html', context={'tag': new_tag})
        return render(request, 'blog/tag_update_form.html', context={'form': form, 'tag': tag})


class PostUpdate(View):
    """Изменяет пост"""

    def get(self, request, slug):
        """Показывает форму с заполненными полями"""
        post = Post.objects.get(slug__iexact=slug)
        form = PostForm(instance=post)
        template = 'blog/post_update_form.html'
        context = {'post': post, 'form': form}
        return render(request, template, context)

    def post(self, request, slug):
        """Принимает введенные пользователем данные, проверяет валидность данных:
                            если данные валидны, то сохраняет их в базу и показывает страницу с подтверждением;
                            если данные не валидны, то показывает туже самую страницу с формой, что и в GET запросе"""
        post = Post.objects.get(slug__iexact=slug)
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            new_post = form.save()
            return render(request, 'blog/post_create_confirm.html', context={'post': new_post})
        return render(request, 'blog/post_update_form.html', context={'form': form, 'post': post})
