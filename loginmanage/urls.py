from django.urls import path
from loginmanage import views

urlpatterns = [
    path('', views.login),  # 起始页
    path('login', views.login, name='login'),  # 登录系统
    path('quit', views.quit, name='quit'),  # 退出系统
    path('verify_account', views.verify_account),  # 异步验证账号密码
]
handlar404 = 'loginmanage.views.handlar404'
handlar500 = 'loginmanage.views.handlar500'
