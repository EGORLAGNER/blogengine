from django.shortcuts import render


def posts_list(request):
    content = 'LAGNER love Django =)'
    return render(request, 'blog/index.html', context={'text': content})
