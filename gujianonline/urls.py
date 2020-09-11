from django.urls import path  # 处理接口方法
from django.conf import settings  # 全局设置
from django.conf.urls.static import static  # 静态文件
from gujianonline.views import v_role
from gujianonline.views import v_version
from gujianonline.views import v_material
from gujianonline.views import v_material_type
from gujianonline.views import v_goods
from gujianonline.views import v_goods_type


urlpatterns = [
    # 材料
    path("gjol_material_list", v_material.gjol_material_list, name="gjol_material_list"),
    path("gjol_material_add", v_material.gjol_material_add, name="gjol_material_add"),
    path("gjol_material_edit", v_material.gjol_material_edit, name="gjol_material_edit"),
    path("gjol_material_import", v_material.gjol_material_import, name="gjol_material_import"),  # 批量导入
    path("gjol_material_adjust", v_material.gjol_material_adjust, name="gjol_material_adjust"),  # 批量调整
    # 材料类型
    path("gjol_goods_type_list", v_goods_type.gjol_goods_type_list, name="gjol_goods_type_list"),
    path("gjol_goods_type_add", v_goods_type.gjol_goods_type_add, name="gjol_goods_type_add"),
    path("gjol_goods_type_edit", v_goods_type.gjol_goods_type_edit, name="gjol_goods_type_edit"),
    # 物品
    path("gjol_goods_list", v_goods.gjol_goods_list, name="gjol_goods_list"),
    path("gjol_goods_add", v_goods.gjol_goods_add, name="gjol_goods_add"),
    path("gjol_goods_edit", v_goods.gjol_goods_edit, name="gjol_goods_edit"),
    path("gjol_goods_recipe", v_goods.gjol_goods_recipe, name="gjol_goods_recipe"),  # 配方
    # path("gjol_material_import", v_goods.gjol_material_import, name="gjol_material_import"),  # 批量导入
    # path("gjol_material_adjust", v_goods.gjol_material_adjust, name="gjol_material_adjust"),  # 批量调整
    # 物品类型
    path("gjol_material_type_list", v_material_type.gjol_material_type_list, name="gjol_material_type_list"),
    path("gjol_material_type_add", v_material_type.gjol_material_type_add, name="gjol_material_type_add"),
    path("gjol_material_type_edit", v_material_type.gjol_material_type_edit, name="gjol_material_type_edit"),
    # 版本
    path("gjol_version_list", v_version.gjol_version_list, name="gjol_version_list"),
    path("gjol_version_add", v_version.gjol_version_add, name="gjol_version_add"),
    path("gjol_version_edit", v_version.gjol_version_edit, name="gjol_version_edit"),
    # 角色
    path("gjol_role_list", v_role.gjol_role_list, name="gjol_role_list"),
    path("gjol_role_add", v_role.gjol_role_add, name="gjol_role_add"),
    path("gjol_role_edit", v_role.gjol_role_edit, name="gjol_role_edit"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
