
from django.urls import path
from . import viwes
urlpatterns = [
    path("", viwes.home, name = 'home'),
    path("count", viwes.count, name='count'),
    path("about",viwes.about_us,name = 'about'),
]
