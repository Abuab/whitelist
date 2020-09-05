from django import forms
from django.shortcuts import render
from . import models
from .models import Ip
import re
from django.core.exceptions import ValidationError

user=['初夏','90','阿水','阿东','阿略','阿衰']

def ip_valinum(value):
    ip_re=re.compile(r'(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])')
    if not ip_re.match(value):
        raise ValidationError('IP格式错误，请重新输入')

def user_valinum(value):
    if value not in user:
        raise ValidationError("添加人请填写：初夏,90,阿水,阿东,阿略,阿衰，如若不在此范围内禁止提交")

class AddipForm(forms.Form):
    model=Ip
    hostname_list=(
        (0,'bw'),
        (1,'ky'),
        (2,'fw'),
        (3,'yn'),
        (4,'ys'),
        (5,'hn'),
    )
    Form_ip=forms.CharField(max_length=15,validators=[ip_valinum,],
                           error_messages={'required':u'IP地址不能为空'},
                           widget=forms.TextInput(attrs={'class':"form-control",'placeholder':u'IP地址'})
                           )
    Form_username=forms.CharField(max_length=30,validators=[user_valinum],
                                 error_messages={'required':u'添加人不能为空'},
                                 widget=forms.TextInput(attrs={'class':"form-control",'placeholder':u'添加人姓名'}))
    Form_hostname=forms.IntegerField(widget=forms.widgets.Select(choices=hostname_list,attrs={'class':'form-control'}))
