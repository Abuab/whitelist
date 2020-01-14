from django import forms
from django.shortcuts import render
from . import models
from .models import Ip
import re
from django.core.exceptions import ValidationError

def ip_valinum(value):
    #ip_re=re.compile(r'([1-9]{3}\.[0-9]{3}\.[0-9]{3}\.)[0-9]{3}')
    ip_re=re.compile(r'(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])')
    if not ip_re.match(value):
        raise ValidationError('IP格式错误，请重新输入')

class AddipForm(forms.Form):
    model=Ip
    hostname_list=(
        (0,'百万'),
        (1,'开元'),
        (2,'富翁'),
        (3,'银牛'),
        (4,'勇胜'),
        (5,'红牛'),
    )
    Form_ip=forms.CharField(max_length=15,validators=[ip_valinum,],
                           error_messages={'required':u'IP地址不能为空'},
                           widget=forms.TextInput(attrs={'class':"form-control",'placeholder':u'IP地址'})
                           )
    Form_username=forms.CharField(max_length=30,error_messages={'required':u'添加人不能为空'})
    Form_hostname=forms.IntegerField(widget=forms.widgets.Select(choices=hostname_list,attrs={'class':'form-control'}))
