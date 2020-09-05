# -*- coding:utf-8 -*-
import subprocess
import sys
import telegram
import time
from io import StringIO
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators import csrf
from .forms import AddipForm

host={'bw':'4xx7.xx.xx.xx','ky':'xx.xx.xx.xx','ys':'xx.xx.xx.xx','hn':'xx.xx.xx.xx','yn':'xx.xx.xx.xx','fw':'4xx7.xx.xx.x'}
whiteip=['61.244.66.114']

def hello(request):
    return render(request,'hello.html')

def addip(request):
    x_forwarded_for=request.META.get("HTTP_X_FORWARDED_FOR","")
    if not x_forwarded_for:
        x_forwarded_for=request.META.get('REMOTE_ADDR',"")
    client_ip=x_forwarded_for.split(",")[-1].strip() if x_forwarded_for else ""
    if client_ip not in whiteip:
        return render(request,'userprofile/error.html')
    if request.method == 'POST':
        form = AddipForm(request.POST,request.FILES)
        hostname_list=(
            (0,'bw'),
            (1,'ky'),
            (2,'fw'),
            (3,'yn'),
            (4,'ys'),
            (5,'hn'),
        )
        if form.is_valid():
            alldata=form.clean()
            ip=alldata['Form_ip'].strip()
            host_name=hostname_list[alldata['Form_hostname']][1]
            username=alldata['Form_username']
            hostname=host[host_name]

            comm=f"bash /data/ops/django/abu/whitelist/fabric.sh '{hostname}' '{ip}'"
            result=subprocess.getstatusoutput(comm)

            x_forwarded_for=request.META.get("HTTP_X_FORWARDED_FOR","")
            if not x_forwarded_for:
                x_forwarded_for=request.META.get('REMOTE_ADDR',"")
            client_ip=x_forwarded_for.split(",")[-1].strip() if x_forwarded_for else ""

            file="/data/ops/django/abu/whitelist/operation.log"
            da_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            oplog="操作时间：%s 操作人：%s 登录IP：%s 平台名称：%s 添加的IP：%s" % (da_time,username,client_ip,host_name,ip)

            with open(file,'a+') as f:
                f.write(oplog+'\n')

            chat_id = '-1001311439088'
            bot = telegram.Bot(token='1039861974:AAHy4xc_hWPqysYEtmJipuytxIdjH_2h4YQ')
            msg="""操作时间：%s
操作人：%s
登录IP：%s
平台名称：%s
添加的IP：%s""" % (da_time,username,client_ip,host_name,ip)
            bot.send_message(chat_id=chat_id,text=msg)
            return render(request,'return.html')
            #return HttpResponse('{"status":"sunness"}',content_type='application/json')
        else:
            error=form.errors
            return render(request,'index.html',{'form':form,'error':error})
    else:
        form=AddipForm()
    return render(request,'index.html',{'form':form})

def oplog(request):
    x_forwarded_for=request.META.get("HTTP_X_FORWARDED_FOR","")
    if not x_forwarded_for:
        x_forwarded_for=request.META.get('REMOTE_ADDR',"")
    client_ip=x_forwarded_for.split(",")[-1].strip() if x_forwarded_for else ""
    if client_ip not in whiteip:
        return render(request,'userprofile/error.html')
    fo=open('/data/ops/django/abu/whitelist/operation.log','r')
    list=fo.readlines()
    return render(request,'oplog.html',{'alist':list})
