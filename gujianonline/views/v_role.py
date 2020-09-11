from gujianonline.views_base import *


# 材料类型：列表
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_role_list(request):
    # 菜单栏点击触发
    if ("iframe_id" in request.GET):
        return render(request, "role/list.html")

    else:  # table.render中的url跳转
        page = request.GET.get("page")
        limit = request.GET.get("limit")
        name = request.GET.get("name", "").strip()

        raw_data = list(GJOL_Role.objects.filter(Q(is_del=0) & Q(name__contains=name)).values())
        page_inator = Paginator(raw_data, limit)
        contacts = page_inator.page(page)
        data_list = []
        for contact in contacts:
            data_list.append(contact)

        res = {}
        res["code"] = 0
        res["msg"] = "success"
        res["data"] = data_list
        res["count"] = len(raw_data)
        return JsonResponse(res)


# 材料类型：新增
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_role_add(request):
    if request.method == 'GET':
        return render(request, "role/edit.html", {"path": "gjol_role_add"})

    else:
        name = request.POST.get('name')
        profession = request.POST.get('profession')
        sort = request.POST.get('sort')
        create_date = request.POST.get('create_date')
        server_info = request.POST.get('server_info')
        account_info = request.POST.get('account_info')
        remark = request.POST.get('remark')
        create_by = request.session.get('user_id')

        role = GJOL_Role(
            name=name,
            profession=profession,
            sort=sort,
            create_date=set_default_date(create_date),
            server_info=server_info,
            account_info=account_info,
            remark=remark,
            create_by=create_by)
        role.save()
        res = {"msg": "新增成功!"}
        return JsonResponse(res)


# 材料类型：编辑
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_role_edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        raw_data = list(GJOL_Role.objects.filter(id=id).values())
        return render(request, "role/edit.html", {"role_list": raw_data, "path": "gjol_role_edit"})

    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        profession = request.POST.get('profession')
        sort = request.POST.get('sort')
        create_date = request.POST.get('create_date')
        server_info = request.POST.get('server_info')
        account_info = request.POST.get('account_info')
        remark = request.POST.get('remark')
        GJOL_Role.objects.filter(id=id).update(
            name=name,
            profession=profession,
            sort=sort,
            create_date=set_default_date(create_date),
            server_info=server_info,
            account_info=account_info,
            remark=remark)
        res = {"msg": "编辑成功！"}
        return JsonResponse(res)