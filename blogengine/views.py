from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'base.html')


def under_page(request):
    dir_request = dir(request)
    get_request = request.GET
    response = HttpResponse('This is under =)')
    return response
