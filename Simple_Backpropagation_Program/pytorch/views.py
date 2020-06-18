from django.shortcuts import render


# Create your views here.
from pytorch.forms import InputForm


def index(request):
    return render(request, 'index.html', {})


def sub(request):
    context = {'form': InputForm()}
    return render(request, "sub/sub.html", context)
    # return render(request, 'sub/sub.html', {})


def input(request):
    return render(request, "sub/index.html", {})
    # context = {'form': InputForm()}
    # return render(request, "input/input.html", {})

