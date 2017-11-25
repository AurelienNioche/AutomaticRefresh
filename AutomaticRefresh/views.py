from django.shortcuts import render

from time import time


def index(request):

    return render(request, 'base.html', {'time': {"Number of seconds since an obscure date is: ": time()}})


def update(request):
    return render(request, 'update.html', {'time': {"Number of seconds since an obscure date is: ": time()}})

