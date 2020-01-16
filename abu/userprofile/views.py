from django.shortcuts import render,redirect
from . import models
from .forms import UserForm,RegisterForm
import hashlib
import requests


def login(request):
    if request.session.get('is_login',None):
        return redirect('/whitelist/addip/')
    if request.method == 'POST':
        login_form=UserForm(request.POST)
        message="请检查填写的内容"
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            try:
                user=models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login']=True
                    request.session['user_id']=user.id
                    request.session['user_name']=user.name
                    return redirect('/whitelist/addip/')
                else:
                    message="密码不正确"
            except:
                message="用户不存在"
        return render(request,'userprofile/login.html',locals())
    login_form=UserForm()
    return render(request,'userprofile/login.html',locals())

def register(request):
    if request.session.get('is_login',None):
        return redirect('/whitelist/addip/')
    if request.method == 'POST':
        register_form=RegisterForm(request.POST)
        message="请检查填写的内容"
        if register_form.is_valid():
            username=register_form.cleaned_data['username']
            password1=register_form.cleaned_data['password1']
            password2=register_form.cleaned_data['password2']
            sex=register_form.cleaned_data['sex']
            if password1 != password2:
                message="两次输入的密码不同"
                return render(request,'userprofile/register.html',locals())
            else:
                same_name_user=models.User.objects.filter(name=username)
                if same_name_user:
                    message="用户已经存在，请重新选择用户名"
                    return render(request,'userprofile/register.html',locals())
                new_user=models.User.objects.create()
                new_user.name=username
                new_user.password=hash_code(password1)
                new_user.sex=sex
                new_user.save()
                return redirect('/userprofile/login/')
    register_form=RegisterForm()
    return render(request,'userprofile/register.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('whitelist:addip')
    request.session.flush()
    return redirect('whitelist:addip')

def hash_code(s,salt='mysite_login'):
    h=hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
