from django.template import RequestContext
from django.shortcuts import render


# views.py
def some_view(request):
    return render(template_name='resume/resume_body.html', request=request)