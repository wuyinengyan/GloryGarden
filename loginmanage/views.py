from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout  # 退出session
from loginmanage.util import *  # 自定义工具类


# def index(request):
#     return render(request, 'login/login.html')

# 登陆
@csrf_protect
def login(request):
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    if request.method == 'GET':  # 如果是get请求
        quit(request)  # 只要登录页面，清除以前用户session
        return render(request, 'login/login.html', {'path': path, 'ff_path': ff_path})  # 交给前台
    else:
        username = request.POST.get("username")  # 获取前台post 提交的username
        password = request.POST.get("password")  # 获取前台post 提交的password
        print(username, password)
        # 查询用户是否存在
        try:
            db_username = User.objects.get(user_name=username)
        except User.DoesNotExist as e:
            info = {"info": "账号或密码错误"}
            return JsonResponse(info)

        # 如果存在,验证密码是否正确
        if password != db_username.user_password:
            info = {"info": "账号或密码错误"}
            return JsonResponse(info)

        request.session.set_expiry(10000)
        response = redirect('index')
        token = make_password(username)
        db_username.token = token
        db_username.save()
        response.set_cookie('userToken', token)
        request.session['user_id'] = str(db_username.user_id).replace("-", "")  # 给session放入userid字段(uuid)需要转str之后再替换
        request.session['user_full_name'] = db_username.user_full_name  # 给session放入user_full_name字段
        request.session['user_name'] = db_username.user_name  # 给session放入username字段
        request.session['role_id'] = db_username.role_id  # 给session放入role_id字段
        Online.objects.create(user_id=str(db_username.user_id).replace("-", ""))  # 给上线表插入数据
        return response


# ajax验证
@csrf_protect
def verify_account(request):
    username = request.POST.get("username")  # 获取前台post 提交的username
    password = request.POST.get("password")  # 获取前台post 提交的password
    print(username, password)
    response_data = {"info": "false"}
    try:
        db_username = User.objects.get(user_name=username)
    except User.DoesNotExist as e:
        return JsonResponse(response_data)
    if password != db_username.user_password:
        return JsonResponse(response_data)
    else:
        response_data = {"info": "true"}
        return JsonResponse(response_data)


# 退出方法
@csrf_protect
def quit(request):
    user_id = request.session.get('user_id')
    # Online.objects.filter(user_id=user_id).delete()  # 删除当前用户上线记录
    logout(request)
    return redirect('/index')


# 验证登录
def log_in(info):
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login')
        print('User:%s , Start %s(%s, %s)' % (user_id, info.__name__, args, kwargs))
        return info(request, *args, **kwargs)

    return wrapper


def handlar404(request):
    return render(request, "404.html")


def handlar500(request):
    return render(request, "ztree.html")
