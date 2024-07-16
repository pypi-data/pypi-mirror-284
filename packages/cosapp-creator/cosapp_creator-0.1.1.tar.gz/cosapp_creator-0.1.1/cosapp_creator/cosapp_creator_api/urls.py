from django.urls import path
from . import views


urlpatterns = [
    path("detectConnectionError", views.detectConnectionErrorView),
    path("getLoops", views.getLoops),
]
