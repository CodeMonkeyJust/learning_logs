from django.conf.urls import url
from . import views

app_name = 'users'  # 命名空间定义
urlpatterns = [
    # 登录页面
    url(r'^login/$', views.login, name='login'),
    # 登出页面
    url(r'^logout/$', views.logout, name='logout'),
    # 注册页面
    url(r'^register/$', views.register, name='register'),
]
