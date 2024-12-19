from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .models import Travellerinf,Comments


def home(request):
    comments = Comments.objects.all()
    return render(request, 'home.html', {'comments': comments})


def healthcode(request):
    return render(request, 'healthcode.html')

def travelcode(request):
    return render(request, 'travelcode.html')

def travelguide(request):
    return render(request, 'travelguide.html')

def pcs(request):
    return render(request, 'pcs.html')

def chpolicy(request):
    return render(request, 'chpolicy.html')

def auspolicy(request):
    return render(request, 'auspolicy.html')

def regist(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if password != password2:
            msg = 'Codes typed twice are not the same！'
            return render(request, 'regist.html', locals())
        elif username == '':
            msg = 'Username can not be NULL !'
            return render(request, 'regist.html', locals())
        cuser = User.objects.create_user(username=username, password=password, email=email)
        cuser.save()
        return redirect('/login/')
    return render(request, 'regist.html')


def logins(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        # 用authenticate判断用户名密码是否正确
        if user:
            login(request, user)
            return redirect('/vippage/?' + username)
        else:
            msg = 'Wrong username and password！'
            return render(request, 'login.html', locals())
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/')



class Vippage(View):
    def get(self, request):
        comments = Comments.objects.all()
        return render(request, 'vippage.html',{'comments': comments})



class ContactView(View):
    """处理用户的留言信息"""
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('username', '')
            email = request.POST.get('email', '')
            cs =  request.POST.get('score', '')
            msg = request.POST.get('message', '')
            if name == '':
                msg1 = 'Username can not be NULL !'
                return render(request, 'vippage.html', locals())
            elif cs == '':
                msg1 = 'Score can not be NULL !'
                return render(request, 'vippage.html', locals())

            cuser = Comments(name=name,email=email,cs=cs,msg=msg)
            cuser.save()
            return redirect('/vippage/')









