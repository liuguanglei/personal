from django.http import HttpResponse


def index(request):
    return HttpResponse("welcome to you!")


def hello(request):
    u = request.user
    return HttpResponse("Hello world !")
