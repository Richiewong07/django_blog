from django.conf.urls import url
from . import views

urlpatterns = [

    # r^$ MEANS DON'T ADD ANYTHING TO OUR URL
    # views.index  IS WHAT YOU WANT TO DISPLAY
    # 127.0.0.1/polls/
    url(r'^$', views.post_home, name="post_home"),

]

app_name = 'posts'