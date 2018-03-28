from django.contrib import admin
from django.conf.urls import url

# from . import views # NEED TO IMPORT OUR VIEW FUNCTIONS
#
# urlpatterns = [
#     url(r'^$', views.post_list),            # http://127.0.0.1:8000/posts/
#     url(r'^create/$', views.post_create),   # http://127.0.0.1:8000/posts/create/
#     url(r'^detail/$', views.post_detail),
#     url(r'^update/$', views.post_update),
#     url(r'^delete/$', views.post_delete),
# ]


# ANOTHER WAY TO SET UP URLS
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete
)

urlpatterns = [
    url(r'^$', post_list),                      # http://127.0.0.1:8000/posts/
    url(r'^create/$', post_create),             # http://127.0.0.1:8000/posts/create/
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),         # (?P<id>\d+)$ REG EXORESSION W/ NEW PARAMETER CALLED id --> ONLY ACCEPTS DIGITS
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]