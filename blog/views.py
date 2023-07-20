from django.http import HttpResponse


def posts_list(request):
    return HttpResponse('<h1>Мой блог</h1>')
