from django.shortcuts import render


def posts_list(request):
    content = ['a', 'b', 'c']
    return render(request, 'blog/index.html', context={'text': content})
