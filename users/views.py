from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import views as authview
from django.contrib.auth.forms import UserCreationForm

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            authview.auth_login(request, user)
            return render(request, 'learning_logs/index.html', {})
        else:
            return render(request, 'users/login.html', {})
    else:
        return render(request, 'users/login.html', {})


def logout(request):
    authview.auth_logout(request)
    return render(request, 'learning_logs/index.html', {})


def register(request):
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return render(request, 'learning_logs/index.html', {})
    context = {'form': form}
    return render(request, 'users/register.html', context)
