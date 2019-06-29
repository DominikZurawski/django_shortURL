from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings


from . import views

app_name = 'skroc_url'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^link$', views.skrocone, name='skrocone'),
    url(r'^(?P<short>\w+)$', views.link, name='follow'),
]