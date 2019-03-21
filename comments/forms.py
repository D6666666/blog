#coding=utf-8
#作者：cq
#创建时间：2019/3/21 15:55
#IDE: PyCharm
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']