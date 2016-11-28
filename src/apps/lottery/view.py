from django.http import HttpResponse


def get_newest_term(request):
    return HttpResponse("get_newest_term!")
