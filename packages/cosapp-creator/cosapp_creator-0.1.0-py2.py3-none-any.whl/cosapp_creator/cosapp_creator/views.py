import os
from django.http import HttpResponse
from django.template import loader
from urllib.parse import urljoin

def index(request):
    template = loader.get_template("index.html")
    base_url = os.getenv("COSAPP_CREATOR_API", "http://127.0.0.1:8000")
    cosapp_url = urljoin(base_url, 'api')
    return HttpResponse(template.render({"cosapp_url": cosapp_url}, request))