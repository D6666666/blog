#coding=utf-8
#作者：cq
#创建时间：2019/3/13 14:40
#IDE: PyCharm

from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]