from django.http.response import JsonResponse
from django.http import HttpResponse

def get_qr_pic(request):
    return HttpResponse("get_qr_pic!")