from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def sub(request):
    # if request.method == 'POST':
    #     """
    #     Write down some code which is related to
    #     the number that you input.
    #     """
    #     """
    #     From now you are going to here
    #     to handle the data, you should make database
    #     that helps save data users input numbers into this
    #     Simple BackPropagation Algorithm.
    #     """
    # context = {'form': }
    return render(request, "sub/sub.html", {})
    # return render(request, 'sub/sub.html', {})


def input(request):
    return render(request, "sub/index.html", {})
    # context = {'form': InputForm()}
    # return render(request, "input/input.html", {})
