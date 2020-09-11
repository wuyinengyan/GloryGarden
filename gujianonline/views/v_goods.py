from gujianonline.views_base import *
from django.db import connection


# 商品：列表
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_goods_list(request):
    # 菜单栏点击触发
    if ("iframe_id" in request.GET):
        version_list = list(GJOL_Version.objects.filter(is_del=0).values("id", "short_name"))
        type_list = list(GJOL_Goods_Type.objects.filter(is_del=0).values("id", "name"))
        return render(request, "goods/list.html", {"version_list": version_list,
                                                      "type_list": type_list})
    # 加载数据
    else:  # table.render中的url跳转
        page = request.GET.get("page")
        limit = request.GET.get("limit")
        name = request.GET.get("name", "").strip()
        version_id = request.GET.get("version_id", "")
        type_id = request.GET.get("type_id", "")

        where = " where 1=1"
        if len(name):
            where += " and name like '%%" + name + "%%'"
        if len(version_id):
            where += " and version_id = '" + version_id.replace('-', '') + "'"
        if len(type_id):
            where += " and type_id = '" + type_id.replace('-', '') + "'"
        raw_sql = "SELECT * FROM view_get_gjol_goods_list" + where
        raw_data = GJOL_Goods.objects.raw(raw_sql)
        raw_list = transfer_rawqueryset_to_list(raw_data)  # 把RawQuerySet转化为list
        page_inator = Paginator(raw_list, limit)
        contacts = page_inator.page(page)  # 请求第几页数据
        data_list = []  # 最终返回的结果集合
        for contact in contacts:
            data_list.append(contact)

        res = {}
        res["code"] = 0
        res["msg"] = "success"
        res["data"] = data_list
        res["count"] = len(raw_list)
        return JsonResponse(res)


# 商品：新增
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_goods_add(request):
    if request.method == 'GET':
        version_list = list(GJOL_Version.objects.filter(is_del=0).values("id", "short_name"))
        type_list = list(GJOL_Goods_Type.objects.filter(is_del=0).values("id", "name"))
        return render(request, "goods/edit.html", {"path": "gjol_goods_add",
                                                      "version_list": version_list,
                                                      "type_list": type_list})

    else:
        name = request.POST.get('name')
        version_id = request.POST.get('version_id')
        type_id = request.POST.get('type_id')
        sort = request.POST.get('sort')
        fee = request.POST.get('fee')
        description = request.POST.get('description')
        create_by = request.session.get('user_id')  # 登录用户为创建人

        goods = GJOL_Goods(
            name=name,
            version_id=version_id,
            type_id=type_id,
            sort=sort,
            fee=fee,
            description=description,
            create_by=create_by)
        goods.save()
        res = {"msg": "新增成功!"}
        return JsonResponse(res)


#  商品：编辑
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_goods_edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        goods_info = list(GJOL_Goods.objects.filter(id=id).values())
        version_list = list(GJOL_Version.objects.filter(is_del=0).values("id", "short_name"))
        type_list = list(GJOL_Goods_Type.objects.filter(is_del=0).values("id", "name"))
        return render(request, "goods/edit.html", {"path": "gjol_goods_edit",
                                                      "goods_info": goods_info,
                                                      "version_list": version_list,
                                                      "type_list": type_list})

    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        version_id = request.POST.get('version_id')
        type_id = request.POST.get('type_id')
        sort = request.POST.get('sort')
        fee = request.POST.get('fee')
        description = request.POST.get('description')
        GJOL_Goods.objects.filter(id=id).update(
            name=name,
            version_id=version_id,
            type_id=type_id,
            sort=sort,
            fee=fee,
            description=description)
        res = {"msg": "编辑成功！"}
        return JsonResponse(res)



@csrf_protect
@log_in
@xframe_options_exempt
# 商品：配方
def gjol_goods_recipe(request):
    if request.method == "GET":
        material_list = list(GJOL_Material.objects.filter(is_del=0).values("id", "name"))
        goods_list = list(GJOL_Goods.objects.filter(is_del=0).values("id", "name"))

        component_type = request.GET.get("type", "")
        if len(component_type):
            value_list = choose_list_data_source(component_type, material_list, goods_list)
            res = {
                "status": True,
                "data": value_list}
            return JsonResponse(res)

        goods_id = request.GET.get("goods_id")

        component_list = list(GJOL_Goods_Component.objects.filter(goods_id=goods_id))
        component_count = len(component_list)
        value_list_list = [[]] * 5
        for i in range(5):
            if component_count > i:
                value_list_list[i] = choose_list_data_source(component_list[i].component_type, material_list, goods_list)

        return render(request, "goods/recipe.html", {"path": "gjol_goods_recipe",
                                                     "component_list": component_list,
                                                     "component_count": component_count,
                                                     "value1_list": value_list_list[0],
                                                     "value2_list": value_list_list[1],
                                                     "value3_list": value_list_list[2],
                                                     "value4_list": value_list_list[3],
                                                     "value5_list": value_list_list[4],})
    # 保存：POST
    else:
        res = {"msg": "保存失败!"}
        goods_id = request.POST.get("goods_id", "")
        create_by = request.session.get('user_id')  # 登录用户为创建人

        components_list = []
        type1 = request.POST.get("type1")
        type2 = request.POST.get("type2")
        type3 = request.POST.get("type3")
        type4 = request.POST.get("type4")
        type5 = request.POST.get("type5")
        if type1 != "-1":
            value1 = request.POST.get("value1")
            text1 = request.POST.get("text1")
            amount1 = request.POST.get("amount1")
            component = GJOL_Goods_Component(create_by=create_by,
                                             goods_id=goods_id,
                                             component_type=type1,
                                             component_id=value1.replace('-', ''),
                                             component_name=text1,
                                             amount=amount1,
                                             sort=1)
            components_list.append(component)
        if type2 != "-1":
            value2 = request.POST.get("value2")
            text2 = request.POST.get("text2")
            amount2 = request.POST.get("amount2")
            component = GJOL_Goods_Component(create_by=create_by,
                                             goods_id=goods_id,
                                             component_type=type2,
                                             component_id=value2.replace('-', ''),
                                             component_name=text2,
                                             amount=amount2,
                                             sort=2)
            components_list.append(component)
        if type3 != "-1":
            value3 = request.POST.get("value3")
            text3 = request.POST.get("text3")
            amount3 = request.POST.get("amount3")
            component = GJOL_Goods_Component(create_by=create_by,
                                             goods_id=goods_id,
                                             component_type=type3,
                                             component_id=value3.replace('-', ''),
                                             component_name=text3,
                                             amount=amount3,
                                             sort=3)
            components_list.append(component)
        if type4 != "-1":
            value4 = request.POST.get("value4")
            text4 = request.POST.get("text4")
            amount4 = request.POST.get("amount4")
            component = GJOL_Goods_Component(create_by=create_by,
                                             goods_id=goods_id,
                                             component_type=type4,
                                             component_id=value4.replace('-', ''),
                                             component_name=text4,
                                             amount=amount4,
                                             sort=4)
            components_list.append(component)
        if type5 != "-1":
            value5 = request.POST.get("value5")
            text5 = request.POST.get("text5")
            amount5 = request.POST.get("amount5")
            component = GJOL_Goods_Component(create_by=create_by,
                                             goods_id=goods_id,
                                             component_type=type5,
                                             component_id=value5.replace('-', ''),
                                             component_name=text5,
                                             amount=amount5,
                                             sort=5)
            components_list.append(component)

        GJOL_Goods_Component.objects.filter(goods_id=goods_id).delete()  # 批量删除
        if components_list:
            GJOL_Goods_Component.objects.bulk_create(components_list)
            with connection.cursor() as cursor:
                cursor.callproc('proc_set_gjol_goods_price', (goods_id.replace('-', ''),))  # 注意参数应该是一个元组
            res = {"msg": "保存成功!"}
        return JsonResponse(res)


# 选择数据源
def choose_list_data_source(component_type, li1, li2):
    if component_type == "material":
        return li1
    elif component_type == "goods":
        return li2
    return []


# 把RawQuerySet转化为list
# ^LHJNote 2020年9月9日15:27:57$
def transfer_rawqueryset_to_list(raw_data):
    raw_list = []
    for obj in raw_data:
        dic = {}
        dic["id"] = obj.id
        dic["name"] = obj.name
        dic["type_id"] = obj.type_id
        dic["type_name"] = obj.type_name
        dic["version_id"] = obj.version_id
        dic["version_name"] = obj.version_name
        dic["sort"] = obj.sort
        dic["price"] = obj.price
        dic["fee"] = obj.fee
        dic["description"] = obj.description
        dic["is_del"] = obj.is_del
        dic["recipe_components"] = obj.recipe_components
        raw_list.append(dic)
    return raw_list