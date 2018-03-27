from django.contrib import admin
from django.conf.urls import url

from . import views # NEED TO IMPORT OUR VIEW FUNCTIONS

urlpatterns = [
    url(r'^$', views.post_list),            # http://127.0.0.1:8000/posts/
    url(r'^create/$', views.post_create),   # http://127.0.0.1:8000/posts/create/
    url(r'^detail/$', views.post_detail),
    url(r'^update/$', views.post_update),
    url(r'^delete/$', views.post_delete),
]