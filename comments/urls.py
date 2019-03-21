#coding=utf-8
#作者：cq
#创建时间：2019/3/21 16:06
#IDE: PyCharm
from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]