#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'LML_CH'
__mtime__ = '2015/3/23'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(required=True,max_length=30,error_messages={'required':u'用户名不能为空'})
    email = forms.EmailField(required=True,error_messages={'required':u'邮箱不能为空','invalid':u'请输入正确的邮箱'})
    passwd = forms.CharField(required=True,widget=forms.PasswordInput(),error_messages={'required':u'密码不能为空'})

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=True,
        label=u"用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )
    passwd = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }
        ),
    )
     # def clean(self):
     #    if not self.is_valid():
     #        raise forms.ValidationError(u"用户名和密码为必填项")
     #    else:
     #        return self.cleaned_data
