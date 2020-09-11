from django.shortcuts import *
from django.db.models import Q, Avg, Max, Min, Count, Sum
from django.views.decorators.csrf import csrf_protect
from loginmanage.util import *  # 自定义工具类
from django.db import connection
from django.contrib.auth import logout  # 退出session
import os, zipfile
from loginmanage.views import log_in
from django.core.paginator import Paginator  # Django内置分页功能模块
from django.views.decorators.clickjacking import xframe_options_exempt

'''
检查sql输出 
connection模块：connection.queries
django原始QuerySet： 后面加   .query
'''


# 首页模版
@csrf_protect
@log_in
def index(request):
    user_id = request.session.get('user_id')
    user_item = list(User.objects.filter(user_id=user_id).values())  # 信息项
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    return render(request, "index.html", {'ff_path': ff_path, 'path': path,
                                          'homepage': Menu.objects.filter(name="首页", parent__isnull=True),
                                          'leftmenu': Menu.objects.filter(parent__isnull=False, is_active=1,
                                                                          tree_id=12),
                                          'topmenu': Menu.objects.filter(~Q(name="首页"), parent__isnull=True),
                                          'user_item': user_item,
                                          })


# 保存用户主题
@csrf_protect
@log_in
def check_theme(request):
    if request.method == 'POST':
        login_user = request.session.get('user_id')
        theme = request.POST.get('theme')
        _u = User.objects.filter(user_id=login_user).update(theme=theme, updateby=login_user)
        munu_list = {"info": "主题修改成功"}
        return JsonResponse(munu_list)


# 菜单列表页
@csrf_protect
@log_in
@xframe_options_exempt
def menu_page(request):
    user_id = request.session.get('user_id')
    iframe_id = request.GET.get('iframe_id')  # 模版菜单id
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    munu_button_rights = {}
    munu_button_rights['role_create_rights'] = role_create_rights(user_id, iframe_id)
    munu_button_rights['role_delete_rights'] = role_delete_rights(user_id, iframe_id)
    munu_button_rights['role_update_rights'] = role_update_rights(user_id, iframe_id)
    munu_button_rights['role_select_rights'] = role_select_rights(user_id, iframe_id)
    return render(request, "menu/menu_list.html",
                  {'ff_path': ff_path, 'path': path, 'munu_button_rights': munu_button_rights
                   })


# 菜单数据
@csrf_protect
@log_in
@xframe_options_exempt
def menu_data(request, *args, **kwargs):
    parent_id = request.GET.get('pid')  # 左侧树点击id
    name = request.GET.get('name')  # 按name查询

    page = request.GET.get('page')  # 页面
    limit = request.GET.get('limit')  # 条数
    munu_list = {}
    datas = list(Menu.objects.filter(is_active=1).values())  # 实例数据库查的数据
    munu_list['count'] = Menu.objects.filter(is_active=1).count()
    # 如果点击左树
    if parent_id:
        parent_list = Menu.objects.get(id=parent_id)
        datas = list(
            Menu.objects.filter(~Q(id=parent_list.id), is_active=1, parent_id=parent_list.id).values())  # 实例数据库查的数据
        munu_list['count'] = Menu.objects.filter(~Q(id=parent_list.id), is_active=1,
                                                 parent_id=parent_list.id).count()  # 条数
    # 如果按名字查询
    if name:
        datas = list(Menu.objects.filter(name__icontains=name).values())  # 实例数据库查的数据
        munu_list['count'] = Menu.objects.filter(name__icontains=name).count()  # 条数
    page_inator = Paginator(datas, limit)  # 分页
    contacts = page_inator.page(page)  # 请求第几页数据
    res = []  # 最终返回的结果集合
    for contact in contacts:
        res.append(contact)
    munu_list['code'] = 0
    munu_list['msg'] = 'success'
    munu_list['data'] = res
    return JsonResponse(munu_list)


# 用户列表页
@csrf_protect
@log_in
@xframe_options_exempt
def user_page(request):
    user_id = request.session.get('user_id')
    iframe_id = request.GET.get('iframe_id')  # 模版菜单id
    user_button_rights = {}
    user_button_rights['role_create_rights'] = role_create_rights(user_id, iframe_id)
    user_button_rights['role_delete_rights'] = role_delete_rights(user_id, iframe_id)
    user_button_rights['role_update_rights'] = role_update_rights(user_id, iframe_id)
    user_button_rights['role_select_rights'] = role_select_rights(user_id, iframe_id)
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    return render(request, "user/user_list.html",
                  {'ff_path': ff_path, 'path': path, 'user_button_rights': user_button_rights})


# 用户数据
@csrf_protect
@log_in
@xframe_options_exempt
def user_data(request):
    page = request.GET.get('page')  # 页面
    limit = request.GET.get('limit')  # 条数
    user_list = {}
    datas = list(User.objects.filter(is_active=1).values())
    page_inator = Paginator(datas, limit)  # 分页
    contacts = page_inator.page(page)  # 请求第几页数据
    res = []  # 最终返回的结果集合
    for contact in contacts:
        res.append(contact)
    user_list['code'] = 0
    user_list['msg'] = 'success'
    user_list['data'] = res
    user_list['count'] = User.objects.filter(is_active=1).count()
    return JsonResponse(user_list)


@csrf_protect
@log_in
@xframe_options_exempt
# 用户添加
def user_add(request):
    user_id = request.session.get('user_id')
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    role_list = {}
    role_list['data'] = list(Role.objects.filter(~Q(role_id=1), is_active=1).values())
    if request.method == 'GET':
        return render(request, "user/user_edit.html",
                      {'ff_path': ff_path, 'path': path, 'role_list': role_list, 'user_id': user_id})
    else:

        role = request.POST.get('role')
        user_full_name = request.POST.get('user_full_name')
        user_name = request.POST.get('user_name')
        user_password = '123456'
        user_email = request.POST.get('user_email')
        user_sex = request.POST.get('user_sex')
        user_card = request.POST.get('user_card')
        user_phone_number = request.POST.get('user_phone_number')
        is_active = request.POST.get('is_active')
        createby = request.POST.get('createby')
        updateby = request.POST.get('updateby')
        img_url = request.FILES.get('image')
        create_user = User(role_id=role,
                           user_full_name=user_full_name,
                           user_name=user_name,
                           user_password=user_password,
                           user_email=user_email,
                           user_sex=user_sex,
                           user_card=user_card,
                           user_phone_number=user_phone_number,
                           is_active=is_active,
                           createby=createby,
                           updateby=updateby,
                           img_url=img_url)
        create_user.save()
        response_data = {"info": "成功添加角色"}
        return JsonResponse(response_data)


@csrf_protect
@log_in
@xframe_options_exempt
# 用户详情
def user_info(request):
    user_id = request.session.get('user_id')
    user_list_id = str(request.GET.get('user_list_id')).replace('-', '')
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    role_list = {}
    role_list['data'] = list(Role.objects.filter(~Q(role_id=1), is_active=1).values())
    user_list = {}
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT users.user_id , users.user_full_name , users.user_name , users.user_password , users.user_email , users.user_sex ,users.user_phone_number,users.user_card,users.createby,users.updateby,users.is_active,users.img_url,users.role_id,role.role_id,role.role_name FROM sys_user users LEFT JOIN sys_role role ON users.role_id = role.role_id AND role.is_active = '1' WHERE users .is_active = 1 AND user_id = % s",
            [user_list_id]
        )
        user_list['data'] = dictfetchall(cursor)
    print(connection.queries)
    return render(request, "user/user_info.html",
                  {'ff_path': ff_path, 'path': path, 'role_list': role_list, 'user_id': user_id,
                   'user_list': user_list['data'], 'user_list_id': user_list_id})


@csrf_protect
@log_in
@xframe_options_exempt
# 用户删除
def user_del(request):
    if request.method == 'GET':
        user_list_id = request.GET.get('user_list_id')
        role_list = {}
        role_list['data'] = list(Role.objects.filter(~Q(role_id=1), is_active=1).values())
        user_list = {}
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT users.user_id , users.user_full_name , users.user_name , users.user_password , users.user_email , users.user_sex ,users.user_phone_number,users.user_card,users.createby,users.updateby,users.is_active,users.img_url,users.role_id,role.role_id,role.role_name FROM sys_user users LEFT JOIN sys_role role ON users.role_id = role.role_id AND role.is_active = '1' WHERE users .is_active = 1 AND user_id = % s",
                [user_list_id]
            )
            user_list['data'] = dictfetchall(cursor)
        response_data = "   您确定要删除吗"
        return HttpResponse(response_data)
    else:
        user_id = request.POST.get('user_id')
        print()
        User.objects.filter(user_id=user_id).delete()
        del_info = {}
        del_info['status'] = 'true'
        del_info['info'] = '已删除'
        return JsonResponse(del_info)


@csrf_protect
@log_in
@xframe_options_exempt
# 用户编辑
def user_edit(request):
    login_user = request.session.get('user_id')
    user_list_id = str(request.GET.get('user_list_id')).replace('-', '')
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    role_list = {}
    role_list['data'] = list(Role.objects.filter(~Q(role_id=1), is_active=1).values())
    user_list = {}
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT users.user_id , users.user_full_name , users.user_name , users.user_password , users.user_email , users.user_sex ,users.user_phone_number,users.user_card,users.createby,users.updateby,users.is_active,users.img_url,users.role_id,role.role_id,role.role_name FROM sys_user users LEFT JOIN sys_role role ON users.role_id = role.role_id AND role.is_active = '1' WHERE users .is_active = 1 AND user_id = % s",
            [user_list_id]
        )
        user_list['data'] = dictfetchall(cursor)
        print(user_list['data'])
    if request.method == 'GET':
        return render(request, "user/user_edit.html",
                      {'ff_path': ff_path, 'path': path, 'role_list': role_list, 'login_user': login_user,
                       'user_list': user_list['data'], 'user_list_id': user_list_id})
    else:
        user_list_id = request.POST.get('user_list_id')
        role = request.POST.get('role')
        user_full_name = request.POST.get('user_full_name')
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_sex = request.POST.get('user_sex')
        user_card = request.POST.get('user_card')
        user_phone_number = request.POST.get('user_phone_number')
        is_active = request.POST.get('is_active')
        createby = request.POST.get('createby')
        updateby = request.POST.get('updateby')
        img_url = request.FILES.get('image')
        print(img_url)
        if img_url:
            _c = User(
                user_id=user_list_id,
                role_id=role,
                user_full_name=user_full_name,
                user_name=user_name,
                user_email=user_email,
                user_sex=user_sex,
                user_card=user_card,
                user_phone_number=user_phone_number,
                is_active=is_active,
                createby=createby,
                updateby=updateby,
                img_url=img_url)
            _c.save()
        if not img_url:
            _u = User.objects.filter(user_id=user_list_id).update(
                role_id=role,
                user_full_name=user_full_name,
                user_name=user_name,
                user_email=user_email,
                user_sex=user_sex,
                user_card=user_card,
                user_phone_number=user_phone_number,
                is_active=is_active,
                createby=createby,
                updateby=updateby)

        response_data = {"info": "成功添加角色"}
        return JsonResponse(response_data)


@csrf_protect
@log_in
@xframe_options_exempt
# 用户修改密码
def user_check_password(request):
    login_user = request.session.get('user_id')
    user_item = list(User.objects.filter(user_id=login_user).values())  # 登录用户信息项
    user_list_id = str(request.GET.get('user_list_id')).replace('-', '')
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url

    if request.method == 'GET':
        user_list_name = list(User.objects.filter(user_id=user_list_id).values('user_full_name'))  # 登录用户信息项
        return render(request, "user/user_check_password.html",
                      {'ff_path': ff_path, 'path': path, 'login_user': login_user,
                       'user_list_id': user_list_id, 'user_item': user_item, 'user_list_name': user_list_name})
    else:
        user_list_id = str(request.POST.get('user_list_id')).replace('-', '')
        user_password = request.POST.get('user_password')
        updateby = request.POST.get('updateby')
        _u = User.objects.filter(user_id=user_list_id).update(
            user_password=user_password,
            updateby=updateby)
        if login_user == user_list_id:
            response_data = {"info": "密码修改成功,请重新登录", "type": "my"}
        else:
            response_data = {"info": "密码修改成功", "type": "other"}
        return JsonResponse(response_data)


# 历史记录
@csrf_protect
@log_in
@xframe_options_exempt
def add_browse_record(request):
    user_id = request.session.get('user_id')
    menu_id = request.GET.get('id')
    response_data = {"info": "已添加"}
    if Browse_record.objects.filter(user_id=user_id).count() >= 8:  # 当前登录用书浏览记录大于等于6条时
        deletelist = Browse_record.objects.get(user_id=user_id, createby=Min('createby')).createby  # 当前用户最早时间浏览记录
        Browse_record.objects.filter(user_id=user_id, createby=deletelist).delete()  # 删除当前用户最早时间浏览记录
        Browse_record.objects.create(user_id=user_id, menu_id=menu_id)  # 创建当前浏览数据
    else:
        Browse_record.objects.create(user_id=user_id, menu_id=menu_id)  # 创建当前浏览数据
    for i in Browse_record.objects.values():
        if Menu.objects.filter(id=i.get('menu_id')).count() == 0:
            Browse_record.objects.filter(menu_id=i.get('menu_id')).delete()
    return JsonResponse(response_data)


# 查询历史记录
@csrf_protect
@log_in
@xframe_options_exempt
def select_browse_record(request):
    user_id = request.session.get('user_id')
    user_id = request.session.get('user_id')
    menu_record_list = {}
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT distinct menu.* FROM  sys_browse_record re left join sys_menu menu on re.menu_id=menu.id WHERE re.user_id = %s  order by re.createby desc",
            [user_id])
        menu_record_list['menu'] = dictfetchall(cursor)
    return JsonResponse(menu_record_list)


# 在线数据
@csrf_protect
@log_in
@xframe_options_exempt
def online_data(request):
    page = request.GET.get('page')  # 页面
    limit = request.GET.get('limit')  # 条数
    online_list = {}
    online_list['code'] = 0
    online_list['msg'] = ''
    datas = ''
    with connection.cursor() as cursor:
        cursor.execute(
            "select onl.online_date,user.user_full_name from sys_online onl left join sys_user user on user.user_id = onl.user_id",
        )
        datas = dictfetchall(cursor)
    datas = list(datas)
    page_inator = Paginator(datas, limit)  # 分页
    contacts = page_inator.page(page)  # 请求第几页数据
    res = []  # 最终返回的结果集合
    for contact in contacts:
        res.append(contact)
    online_list['count'] = Online.objects.count()
    online_list['data'] = res
    return JsonResponse(online_list)


# 在线页面
@csrf_protect
@log_in
@xframe_options_exempt
def online_page(request):
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    return render(request, "online/online_list.html", {'ff_path': ff_path, 'path': path, })


# 强制下线
@csrf_protect
@log_in
@xframe_options_exempt
def online_quit_it(request):
    user_id = request.GET.get('user_id')
    Online.objects.filter(user_id=user_id).delete()  # 删除当前用户上线记录
    logout(request)
    return redirect('/index')


# 角色列表页
@csrf_protect
@log_in
@xframe_options_exempt
def role_page(request):
    user_id = request.session.get('user_id')
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    return render(request, "role/role_list.html", {'ff_path': ff_path, 'path': path, })


# 角色数据
@csrf_protect
@log_in
@xframe_options_exempt
def role_data(request):
    page = request.GET.get('page')  # 页面
    limit = request.GET.get('limit')  # 条数
    role_list = {}
    role_list['code'] = 0
    role_list['msg'] = ''
    role_list['count'] = Role.objects.filter(is_active=1).count()
    datas = list(Role.objects.filter(is_active=1).values())
    page_inator = Paginator(datas, limit)  # 分页
    contacts = page_inator.page(page)  # 请求第几页数据
    res = []  # 最终返回的结果集合
    for contact in contacts:
        res.append(contact)
    role_list['data'] = res
    return JsonResponse(role_list)


# 角色菜单管理树
@csrf_protect
@log_in
@xframe_options_exempt
def role_menu_manage(request):
    role_id = request.GET.get('role_id')  # 点击的角色
    if request.method == 'GET':
        layEvent = request.GET.get('layEvent')  # 点击的按钮
        role = Role.objects.get(role_id=role_id)  # 获取点击角色的数据库信息
        checked = 'true'  # ztree是否带多选框
        rolerights = ''
        if 'role_create_rights' == layEvent:
            rolerights = role.role_create_rights
        elif 'role_delete_rights' == layEvent:
            rolerights = role.role_delete_rights
        elif 'role_update_rights' == layEvent:
            rolerights = role.role_update_rights
        elif 'role_select_rights' == layEvent:
            rolerights = role.role_select_rights
        elif 'role_menu_rights' == layEvent:
            rolerights = role.role_menu_rights
        path = request.scheme + "://" + request.get_host()  # url
        ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
        menu_list = {}
        menu_list['all'] = ''
        if rolerights:
            with connection.cursor() as cursor:
                cursor.execute(
                    "select id,case when parent_id is null then 0 else parent_id end as parent_id,name,case when id in(" + rolerights + ") then 'true' else 'false' end as checked from sys_menu r where 1=1 and r.is_active ='1'"
                )
                menu_list['all'] = dictfetchall(cursor)
        else:
            with connection.cursor() as cursor:
                cursor.execute(
                    "select id,case when parent_id is null then 0 else parent_id end as parent_id,name,'false'  as checked from sys_menu r where 1=1 and r.is_active ='1'"
                )
                menu_list['all'] = dictfetchall(cursor)
        return render(request, "ztree.html",
                      {'ff_path': ff_path, 'path': path, 'menu_list_all': menu_list['all'], 'role_id': role_id,
                       'layEvent': layEvent, 'checked': checked})
    else:
        role_id = request.POST.get('role_id')  # 点击的角色
        layEvent = request.POST.get('layEvent')  # 点击的按钮
        ids = request.POST.get('ids')  # 点击的角色
        response_data = ''
        if 'role_create_rights' == layEvent:
            Role.objects.filter(role_id=role_id).update(role_create_rights=ids)
            response_data = {"info": "成功更新角色添加按钮"}
        elif 'role_delete_rights' == layEvent:
            Role.objects.filter(role_id=role_id).update(role_delete_rights=ids)
            response_data = {"info": "成功更新角色删除按钮"}
        elif 'role_update_rights' == layEvent:
            Role.objects.filter(role_id=role_id).update(role_update_rights=ids)
            response_data = {"info": "成功更新角色编辑按钮"}
        elif 'role_select_rights' == layEvent:
            Role.objects.filter(role_id=role_id).update(role_select_rights=ids)
            response_data = {"info": "成功更新角色查看按钮"}
        elif 'role_menu_rights' == layEvent:
            Role.objects.filter(role_id=role_id).update(role_menu_rights=ids)
            response_data = {"info": "成功更新角色菜单可查看权限"}
        return JsonResponse(response_data)


# 菜单管理树
@csrf_protect
@log_in
@xframe_options_exempt
def menu_list_left_tree(request):
    user_id = request.session.get('user_id')
    if request.method == 'GET':
        path = request.scheme + "://" + request.get_host()  # url
        ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
        checked = 'false'  # ztree是否带多选框
        menu_list = {}
        menu_list['all'] = ''

        with connection.cursor() as cursor:
            cursor.execute(
                "select id,case when parent_id is null then 0 else parent_id end as parent_id,name from sys_menu r where 1=1 and r.is_active ='1'"
            )
            menu_list['all'] = dictfetchall(cursor)
        return render(request, "ztree.html",
                      {'ff_path': ff_path, 'path': path, 'menu_list_all': menu_list['all'], 'checked': checked})


# 菜单管理详情
@csrf_protect
@log_in
@xframe_options_exempt
def menu_info(request):
    menu_id = request.GET.get('menu_id')
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    menu_info = {}
    menu_info['my'] = Menu.objects.get(id=menu_id)
    if not menu_info['my'].parent_id:
        menu_info['parent'] = {'name': "无"}
    else:
        menu_info['parent'] = Menu.objects.get(id=menu_info['my'].parent_id)
    return render(request, "menu/menu_info.html",
                  {'ff_path': ff_path, 'path': path, 'menu_my': menu_info['my'],
                   'menu_parent': menu_info['parent']})


# 菜单管理编辑
@csrf_protect
@log_in
@xframe_options_exempt
def menu_edit(request):
    menu_id = request.GET.get('menu_id')
    if request.method == 'GET':
        path = request.scheme + "://" + request.get_host()  # url
        ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
        menu_info = {}
        menu_info['my'] = Menu.objects.get(id=menu_id)
        menu_info['action'] = 'menu_edit'  # 给前台提交类名
        if not menu_info['my'].parent_id:
            menu_info['parent'] = {'name': ""}
        else:
            menu_info['parent'] = Menu.objects.get(id=menu_info['my'].parent_id)
        return render(request, "menu/menu_edit.html",
                      {'ff_path': ff_path, 'path': path, 'menu_my': menu_info['my'],
                       'menu_parent': menu_info['parent'], 'action': menu_info['action']})
    else:
        my_id = request.POST.get('my_id')
        parent_id = request.POST.get('parent_id')
        name = request.POST.get('name')
        menu_url = request.POST.get('menu_url')
        menu_order = request.POST.get('menu_order')
        menu_icon = request.POST.get('menu_icon')
        menu_type = request.POST.get('menu_type')
        is_active = request.POST.get('is_active')
        _u = Menu.objects.get(id=my_id)  # 点击菜单数据
        # 以下为更新字段
        _u.parent_id = parent_id
        _u.name = name
        _u.menu_url = menu_url
        _u.menu_order = menu_order
        _u.menu_icon = menu_icon
        _u.menu_type = menu_type
        _u.is_active = is_active
        _u.save()
        menu_info = {}
        menu_info['action'] = 'menu_edit'  # 给前台提交类名
        return JsonResponse(menu_info)


# 菜单管理新增
@csrf_protect
@log_in
@xframe_options_exempt
def menu_add(request):
    if request.method == 'GET':
        path = request.scheme + "://" + request.get_host()  # url
        ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
        menu_info = {}
        menu_info['action'] = 'menu_add'
        return render(request, "menu/menu_edit.html",
                      {'ff_path': ff_path, 'path': path, 'action': menu_info['action']})
    else:
        parent_id = request.POST.get('parent_id')
        name = request.POST.get('name')
        menu_url = request.POST.get('menu_url')
        menu_order = request.POST.get('menu_order')
        menu_icon = request.POST.get('menu_icon')
        menu_type = request.POST.get('menu_type')
        is_active = request.POST.get('is_active')
        if parent_id == '':
            Menu.objects.create(name=name, menu_url=menu_url, menu_order=menu_order,
                                menu_icon=menu_icon, menu_type=menu_type, is_active=is_active)  # 创建当前浏览数据
        else:
            Menu.objects.create(parent_id=parent_id, name=name, menu_url=menu_url, menu_order=menu_order,
                                menu_icon=menu_icon, menu_type=menu_type, is_active=is_active)  # 创建当前浏览数据

        menu_info = {}
        menu_info['action'] = 'menu_add'  # 给前台提交类名
        return JsonResponse(menu_info)


# 菜单管理删除
@csrf_protect
@log_in
@xframe_options_exempt
def menu_del(request):
    menu_id = request.GET.get('menu_id')
    if request.method == 'GET':
        _d = Menu.objects.get(id=menu_id)  # 点击菜单数据
        menu_info = {}
        menu_info['info'] = '确定要删除(' + _d.name + ')吗？'  # 给前台提交类名
        return HttpResponse(menu_info['info'])
    else:
        menu_id = request.POST.get('menu_id')
        menu_info = {}
        if Menu.objects.filter(parent_id=menu_id).count() > 0:
            menu_info['status'] = 'false'
            menu_info['info'] = '菜单下存在叶节点，禁止删除'
            return JsonResponse(menu_info)
        else:
            Menu.objects.filter(id=menu_id).delete()  # 删除菜单
            menu_info['status'] = 'true'
            menu_info['info'] = '删除成功'  # 给前台提交类名
            return JsonResponse(menu_info)


# 新加菜单父级选择
@csrf_protect
@log_in
@xframe_options_exempt
def menu_add_parent_tree(request):
    if request.method == 'GET':
        path = request.scheme + "://" + request.get_host()  # url
        ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
        checked = 'true'  # ztree是否带多选框
        menu_list = {}
        menu_list['all'] = ''

        with connection.cursor() as cursor:
            cursor.execute(
                "select id,case when parent_id is null then 0 else parent_id end as parent_id,name from sys_menu r where 1=1 and r.is_active ='1'"
            )
            menu_list['all'] = dictfetchall(cursor)
        return render(request, "menu/add_ztree.html",
                      {'ff_path': ff_path, 'path': path, 'menu_list_all': menu_list['all'], 'checked': checked})
    else:
        response_data = {"info": "成功更新角色添加按钮"}
        return JsonResponse(response_data)


# icon图表列表
@csrf_protect
@log_in
@xframe_options_exempt
def icon_list(request):
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    checked = 'true'  # ztree是否带多选框
    icon_list = {}
    icon_list['all'] = ''

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT dic.dict_id , dic.dict_name , dic.dict_cont , dic.dict_order FROM sys_dictionary dic WHERE dic.parent_id = '64c34f8d6aa249f5baab563bb7906e28' AND dic.is_active = '1'"
        )
        icon_list['all'] = dictfetchall(cursor)
    return render(request, "icon/icon_list.html",
                  {'ff_path': ff_path, 'path': path, 'icon_list': icon_list['all'], 'checked': checked})


# icon图表列表
@csrf_protect
@log_in
@xframe_options_exempt
def check_icon(request):
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    checked = 'true'  # ztree是否带多选框
    icon_list = {}
    icon_list['all'] = ''

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT dic.dict_id , dic.dict_name , dic.dict_cont , dic.dict_order FROM sys_dictionary dic WHERE dic.parent_id = '64c34f8d6aa249f5baab563bb7906e28' AND dic.is_active = '1'"
        )
        icon_list['all'] = dictfetchall(cursor)
    return render(request, "icon/check_icon.html",
                  {'ff_path': ff_path, 'path': path, 'icon_list': icon_list['all'], 'checked': checked})


# 普通代码生成页面
@csrf_protect
@log_in
@xframe_options_exempt
def sublime_test(request):
    response_data = {"info": "else:"}
    return render(request, "sublime_test.html", {'response_data': response_data})


# generate_page
@csrf_protect
@log_in
@xframe_options_exempt
def generate_page(request):
    user_id = request.session.get('user_id')
    iframe_id = request.GET.get('iframe_id')  # 模版菜单id
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    generate_button_rights = {}
    generate_button_rights['role_create_rights'] = role_create_rights(user_id, iframe_id)
    generate_button_rights['role_delete_rights'] = role_delete_rights(user_id, iframe_id)
    generate_button_rights['role_update_rights'] = role_update_rights(user_id, iframe_id)
    generate_button_rights['role_select_rights'] = role_select_rights(user_id, iframe_id)
    return render(request, "generate/generate_list.html",
                  {'ff_path': ff_path, 'path': path, 'generate_button_rights': generate_button_rights
                   })


@csrf_protect
@log_in
@xframe_options_exempt
def generate_data(request):
    user_id = request.session.get('user_id')
    generate_list = {}
    generate_list['code'] = 0
    generate_list['msg'] = ''
    generate_list['count'] = 1000
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM  sys_generate "
        )
        generate_list['data'] = dictfetchall(cursor)
    return JsonResponse(generate_list)


# 菜单管理详情
@csrf_protect
@log_in
@xframe_options_exempt
def generate_info(request):
    user_id = request.session.get('user_id')
    generate_list_id = request.GET.get('generate_list_id')
    path = request.scheme + "://" + request.get_host()  # url
    ff_path = request.scheme + "://" + request.get_host() + request.path  # 加方法url
    generate_info = {}
    generate_info['info'] = Generate.objects.get(generate_id=generate_list_id)
    return render(request, "generate/generate_info.html",
                  {'ff_path': ff_path, 'path': path, 'generate_info': generate_info['info']})


# def file_download(request):
#     content_info = open('./media/generate_file/generate_info.html')
#     with open("./media/my_generate/generate_info.html", "w") as f:
#         for line in content_info:
#             f.write(line.replace("generate", "asd"))
#     file = open('./media/my_generate/generate_info.html', 'r+')
#     response = HttpResponse(file)
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment;filename="generate_info.html"'
#     return response

@csrf_protect
@log_in
@xframe_options_exempt
def file_generate(request):
    class_name = request.POST.get('class_name')
    menu_name = request.POST.get('menu_name')
    content_list = open('./media/generate_file/generate_info.html')
    content_info = open('./media/generate_file/generate_info.html')
    with open("./media/my_generate/" + class_name + "_info.html", "w") as f:
        for line in content_info:
            f.write(line.replace("generate", class_name))
    with open("./media/my_generate/" + class_name + "_list.html", "w") as f:
        for line in content_list:
            f.write(line.replace("generate", class_name).replace("代码测试", menu_name))
    response_data = {"info": "生成成功"}
    return JsonResponse(response_data)


@csrf_protect
@log_in
@xframe_options_exempt
def file_download(request):
    class_name = request.GET.get('class_name')
    menu_name = request.GET.get('menu_name')
    if not class_name and not menu_name:
        with zipfile.ZipFile('./media/generate_file/exportTemplate.zip', 'w') as zipf:
            zipf.write('./media/generate_file/generate_list.html')
            zipf.write('./media/generate_file/generate_info.html')
        z_file = open('./media/generate_file/exportTemplate.zip', 'rb')
        response = HttpResponse(z_file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="online.zip"'
        return response
    else:
        with zipfile.ZipFile('./media/my_generate/myExportTemplate.zip', 'w') as zipf:
            zipf.write('./media/my_generate/' + class_name + '_list.html')
            zipf.write('./media/my_generate/' + class_name + '_info.html')
        z_file = open('./media/my_generate/myExportTemplate.zip', 'rb')
        response = HttpResponse(z_file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="' + class_name + '.zip"'
        os.remove('./media/my_generate/' + class_name + '_list.html')
        os.remove('./media/my_generate/' + class_name + '_info.html')
        return response


@csrf_protect
@xframe_options_exempt
def test(request):
    return render(request, "test.html")
