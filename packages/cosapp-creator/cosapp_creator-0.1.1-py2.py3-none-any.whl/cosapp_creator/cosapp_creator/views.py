import os
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("index.html.j2")
    base_url = os.getenv("COSAPP_CREATOR_BASE_URL", "http://127.0.0.1:8000")
    cosapp_url = f"{base_url.rstrip('/')}/api"
    return HttpResponse(
        template.render({"cosapp_url": cosapp_url, "base_url": base_url}, request)
    )
