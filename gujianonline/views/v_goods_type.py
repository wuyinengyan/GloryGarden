from gujianonline.views_base import *


# 材料类型：列表
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_goods_type_list(request):
    # 菜单栏点击触发
    if ("iframe_id" in request.GET):
        return render(request, "goods_type/list.html")

    else:  # table.render中的url跳转
        page = request.GET.get("page")
        limit = request.GET.get("limit")
        name = request.GET.get("name", "").strip()

        raw_data = list(GJOL_Goods_Type.objects.filter(Q(is_del=0) & Q(name__contains=name)).values())
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


# 材料类型：新增
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_goods_type_add(request):
    if request.method == 'GET':
        return render(request, "goods_type/edit.html", {"path": "gjol_goods_type_add"})

    else:
        name = request.POST.get('name')
        sort = request.POST.get('sort')
        remark = request.POST.get('remark')
        create_by = request.session.get('user_id')

        goods_type = GJOL_Goods_Type(
            name=name,
            sort=sort,
            remark=remark,
            create_by=create_by)
        goods_type.save()
        res = {"msg": "新增成功!"}
        return JsonResponse(res)


# 材料类型：编辑
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_goods_type_edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        raw_data = list(GJOL_Goods_Type.objects.filter(id=id).values())
        return render(request, "goods_type/edit.html", {"goods_type_list": raw_data, "path": "gjol_goods_type_edit"})

    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        sort = request.POST.get('sort')
        remark = request.POST.get('remark')
        GJOL_Goods_Type.objects.filter(id=id).update(
            name=name,
            sort=sort,
            remark=remark,)
        res = {"msg": "编辑成功！"}
        return JsonResponse(res)