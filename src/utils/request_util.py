import os
import logging
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

logger = logging.getLogger(__name__)


def send_file(file_path, filename=None):
    wrapper = FileWrapper(file(file_path))
    response = HttpResponse(wrapper, content_type='application/octet-stream')
    response['Content-Length'] = os.path.getsize(file_path)
    filename = file_path.split(os.sep)[-1] if filename is None else filename
    response['Content-Disposition'] = 'attachment; filename=%s' % filename.encode("utf-8")
    return response


def send_file_content(filename, data):
    response = HttpResponse(data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename.encode("utf-8")
    return response


def getIPFromDJangoRequest(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']
