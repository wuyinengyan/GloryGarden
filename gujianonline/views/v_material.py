from gujianonline.views_base import *
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
from django.http import HttpResponse
import json
from django.db import connection


# 材料：列表
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_material_list(request):
    # 菜单栏点击触发
    if ("iframe_id" in request.GET):
        version_list = list(GJOL_Version.objects.filter(is_del=0).values("id", "short_name"))
        type_list = list(GJOL_Material_Type.objects.filter(is_del=0).values("id", "name"))
        role_list = list(GJOL_Role.objects.filter(is_del=0).values("id", "name"))
        return render(request, "material/list.html", {"version_list": version_list,
                                                      "type_list": type_list,
                                                      "role_list": role_list})

    else:  # table.render中的url跳转
        page = request.GET.get("page")
        limit = request.GET.get("limit")
        name = request.GET.get("name", "").strip()
        priority = request.GET.get("priority", 5)
        version_id = request.GET.get("version_id", "")
        type_id = request.GET.get("type_id", "")
        role_id = request.GET.get("role_id", "")

        q_object = Q(is_del=0) & Q(priority__gte=priority)
        if len(name):
            q_object.add(Q(name__contains=name), Q.AND)
        if len(version_id):
            q_object.add(Q(version_id=version_id), Q.AND)
        if len(type_id):
            q_object.add(Q(type_id=type_id), Q.AND)
        if len(role_id):
            q_object.add(Q(role_id=role_id), Q.AND)
        field_names = (
            "id", "name", "type__name", "version__short_name", "role__name", "priority", "sort", "price", "stock_info",
            "remark", "is_del")
        raw_data = list(GJOL_Material.objects.filter(q_object).values(*field_names))
        page_inator = Paginator(raw_data, limit)
        contacts = page_inator.page(page)  # 请求第几页数据
        data_list = []  # 最终返回的结果集合
        for contact in contacts:
            data_list.append(contact)
            # print(contact.verison.short_name)

        res = {}
        res["code"] = 0
        res["msg"] = "success"
        res["data"] = data_list
        res["count"] = len(raw_data)
        return JsonResponse(res)


# 材料：新增
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_material_add(request):
    if request.method == 'GET':
        version_list = list(GJOL_Version.objects.filter(is_del=0).values("id", "short_name"))
        type_list = list(GJOL_Material_Type.objects.filter(is_del=0).values("id", "name"))
        role_list = list(GJOL_Role.objects.filter(is_del=0).values("id", "name"))
        return render(request, "material/edit.html", {"path": "gjol_material_add",
                                                      "version_list": version_list,
                                                      "type_list": type_list,
                                                      "role_list": role_list})

    else:
        name = request.POST.get('name')
        version_id = request.POST.get('version_id')
        type_id = request.POST.get('type_id')
        priority = request.POST.get('priority')
        sort = request.POST.get('sort')
        price = request.POST.get('price', 0)
        role_id = request.POST.get('role_id')
        stock_info = request.POST.get('stock_info')
        remark = request.POST.get('remark')
        create_by = request.session.get('user_id')  # 登录用户为创建人

        material = GJOL_Material(
            name=name,
            version_id=version_id,
            type_id=type_id,
            priority=priority,
            sort=sort,
            price=price,
            role_id=role_id,
            stock_info=stock_info,
            remark=remark,
            create_by=create_by)
        material.save()
        res = {"msg": "新增成功!"}
        return JsonResponse(res)


#  材料：编辑
@csrf_protect
@log_in
@xframe_options_exempt
def gjol_material_edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        material_info = list(GJOL_Material.objects.filter(id=id).values())
        version_list = list(GJOL_Version.objects.filter(is_del=0).values("id", "short_name"))
        type_list = list(GJOL_Material_Type.objects.filter(is_del=0).values("id", "name"))
        role_list = list(GJOL_Role.objects.filter(is_del=0).values("id", "name"))
        return render(request, "material/edit.html", {"path": "gjol_material_edit",
                                                      "material_info": material_info,
                                                      "version_list": version_list,
                                                      "type_list": type_list,
                                                      "role_list": role_list})

    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        version_id = request.POST.get('version_id')
        type_id = request.POST.get('type_id')
        priority = request.POST.get('priority')
        sort = request.POST.get('sort')
        price = request.POST.get('price', 0)
        role_id = request.POST.get('role_id')
        stock_info = request.POST.get('stock_info')
        remark = request.POST.get('remark')
        GJOL_Material.objects.filter(id=id).update(
            name=name,
            version_id=version_id,
            type_id=type_id,
            priority=priority,
            sort=sort,
            price=price,
            role_id=role_id,
            stock_info=stock_info,
            remark=remark)
        with connection.cursor() as cursor:
            cursor.callproc('proc_recur_update_gjol_goods_price', (id.replace('-', ''),))  # 注意参数应该是一个元组
            # connection.connection.commit()  # 调用存储过程后，确定要进行commit执行
        res = {"msg": "编辑成功！"}
        return JsonResponse(res)



@csrf_protect
@log_in
@xframe_options_exempt
# 材料：批量调整
def gjol_material_adjust(request):
    if request.method == "GET":
        field = request.GET.get("field", "")
        if not len(field):
            return render(request, "material/adjust.html")
        else:
            if field == "version_id":
                # ^LHJNote 2020年9月1日16:30:45$
                # 查询字段重命名
                value_list = list(
                    GJOL_Version.objects.filter(is_del=0).values("id", "short_name").annotate(name=F("short_name")))
            elif field == "type_id":
                value_list = list(GJOL_Material_Type.objects.filter(is_del=0).values("id", "name"))
            elif field == "role_id":
                value_list = list(GJOL_Role.objects.filter(is_del=0).values("id", "name"))
            elif field == "priority":
                value_list = list(({"id": 1, "name": 1}, {"id": 2, "name": 2}, {"id": 3, "name": 3},
                                   {"id": 4, "name": 4}, {"id": 5, "name": 5}))
            else:
                value_list = ""
            res = {
                "status": True,
                "data": value_list}
            return JsonResponse(res)
            # return HttpResponse(json.dumps({"value_list": value_list}))

    else:
        res = {"msg": "调整失败!"}
        field = request.POST.get("field")
        value = request.POST.get("value")
        ids = request.POST.get("ids")

        # id_list = ids.split(",")
        material_list = []
        for field_id in ids.split(","):
            material = GJOL_Material(id=field_id)
            material.__setattr__(field, value)  # 动态给字段赋值
            material_list.append(material)
        if material_list:
            GJOL_Material.objects.bulk_update(material_list, fields=[field])  # 批量编辑指定字段
            res = {"msg": "调整成功!"}
        return JsonResponse(res)


@csrf_exempt
@log_in
@xframe_options_exempt
# 材料：批量导入
def gjol_material_import(request):
    msg = "导入成功！"
    try:
        if request.method == 'POST':
            file = request.FILES.get("file")  # 获取文件信息用 request.FILES.get
            if file:  # 如果文件存在
                data_type = {"price": np.float64, "lmt_price": np.float64, "priority": np.int32, "sort": np.int32}
                df = pd.read_excel(file, dtype=data_type, na_values="", keep_default_na=False)
                if len(df):
                    create_by = request.session.get("user_id")
                    batch_import_data(df, create_by)
                else:
                    raise Exception("文件数据为空！")
            else:
                raise Exception("文件不存在，或已损坏！")
    except Exception as e:
        msg = e
    finally:
        res = {"msg": msg}
        return JsonResponse(res)



# 批量导入数据
def batch_import_data(df, create_by):
    standardize_data([df])  # list相当于C++中的ref引用型参数

    material_list = []
    models_fields = GJOL_Material.get_dict(GJOL_Material()).keys()  # 获取所有字段名称
    for row in range(1, len(df)):
        # models_fields = Material._meta.get_fields()
        material = GJOL_Material(create_by=create_by)
        for column in df.columns:
            if column in models_fields:
                material.__setattr__(column, df.iloc[row][column])  # 动态添加字段
        material_list.append(material)
    if material_list:
        raise Exception("导入成功！")
        # GJOL_Material.objects.bulk_create(material_list)


# 规划并校验数据
def standardize_data(li):
    df = li[0]
    df.fillna("", inplace=True)

    # 必须包含的字段集合
    need_columns = {"name", "version_id", "type_id", "role_id", "price", "lmt_price", "stock_info", "priority", "sort", "remark"}
    columns_set = set(df.columns)  # 转化为集合
    if not need_columns >= columns_set:
        raise Exception("导入文件缺少必须的字段列，请参看模板文件！")


# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.integer):
#             return int(obj)
#         elif isinstance(obj, np.floating):
#             return float(obj)
#         elif isinstance(obj, np.ndarray):
#             return obj.tolist()
#         if isinstance(obj, time):
#             return obj.__str__()
#         else:
#             return super(NpEncoder, self).default(obj)
