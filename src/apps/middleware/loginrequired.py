import logging
from re import compile

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

TIME_OUT = 30 * 60

logger = logging.getLogger(__name__)

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def process_request(self, request):
        try:
            syslockParam = TIME_OUT
            logouttime = int(syslockParam.value)
            request.session.set_expiry(logouttime)
        except Exception:
            request.session.set_expiry(600)
        path = request.path_info.lstrip('/')
        if any(m.match(path) for m in EXEMPT_URLS):
            return
        if hasattr(request, 'user'):
            if not request.user.is_authenticated():
                return HttpResponse("Time out!")
        else:
            return HttpResponse("Time out!")
