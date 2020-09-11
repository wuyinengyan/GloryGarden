from gujianonline.views_base import *


# 版本：列表
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_version_list(request):
    # 菜单栏点击触发
    if ("iframe_id" in request.GET):
        return render(request, "version/list.html")

    else:  # table.render中的url跳转
        page = request.GET.get("page")
        limit = request.GET.get("limit")
        short_name = request.GET.get("short_name", "").strip()

        # kwargs = {}  # 动态查询的字段
        # kwargs["is_del"] = 0
        # if(len(short_name)):
        #     kwargs["short_name"] = short_name
        #     Q(kwargs["short_name"]__contains) = short_name
        raw_data = list(GJOL_Version.objects.filter(Q(is_del=0) & Q(short_name__contains=short_name)).values())
        page_inator = Paginator(raw_data, limit)  # 分页
        contacts = page_inator.page(page)  # 请求第几页数据
        data_list = []  # 最终返回的结果集合
        for contact in contacts:
            data_list.append(contact)

        res = {}
        res["code"] = 0
        res["msg"] = "success"
        res["data"] = data_list
        res["count"] = len(raw_data)
        return JsonResponse(res)


# 版本：新增
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_version_add(request):
    if request.method == 'GET':
        return render(request, "version/edit.html", {"path": "gjol_version_add"})

    else:
        short_name = request.POST.get('short_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        remark = request.POST.get('remark')
        create_by = request.session.get('user_id')  # 登录用户为创建人

        version = GJOL_Version(short_name=short_name,
                               start_date=set_default_date(start_date),
                               end_date=set_default_date(end_date),
                               remark=remark,
                               create_by=create_by)
        version.save()
        res = {"msg": "新增成功!"}
        return JsonResponse(res)


# 版本：编辑
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_version_edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        raw_data = list(GJOL_Version.objects.filter(id=id).values())
        return render(request, "version/edit.html", {"version_list": raw_data, "path": "gjol_version_edit"})

    else:
        id = request.POST.get('id')
        short_name = request.POST.get('short_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        remark = request.POST.get("remark")
        GJOL_Version.objects.filter(id=id).update(
            short_name=short_name,
            start_date=set_default_date(start_date),
            end_date=set_default_date(end_date),
            remark=remark,)
        res = {"msg": "编辑成功！"}
        return JsonResponse(res)