from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.aboutus, name="nosotros"),
    path("carousel/",views.ver_galeria,name="galeria"),
]
