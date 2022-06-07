from django.http import HttpResponse
from django.views.decorators.http import require_GET
import os


@require_GET
def security_txt(request):
    lines = os.getenv('SSL_PKI_VALIDATION').split(' ')
    return HttpResponse("\n".join(lines), content_type="text/plain")