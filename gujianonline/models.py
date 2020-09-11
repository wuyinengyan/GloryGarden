from django.db import models
import django.utils.timezone as timezone
import uuid


# 材料信息表
class GJOL_Material(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, null=False, help_text="提示信息：名称", verbose_name="名称")
    # version_id = models.UUIDField(verbose_name="版本ID")
    # type_id = models.UUIDField(verbose_name="类型ID")
    priority = models.SmallIntegerField(default=1, verbose_name="优先级")
    sort = models.SmallIntegerField(default=99, verbose_name="排序")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="价格")
    lmt_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="最低价")
    stock_info = models.CharField(max_length=40, verbose_name="库存信息")
    remark = models.CharField(max_length=500, verbose_name="备注")
    create_by = models.CharField("创建者", max_length=32, null=False)
    create_time = models.DateTimeField("创建时间", default=timezone.now, null=False)
    update_by = models.CharField("更新者", max_length=32)
    update_time = models.DateTimeField("更新时间")
    is_del = models.BooleanField(default=False)
    # 外键关联
    # on_delete = models.SET_NULL：Material_Type删除后Material置为NULL，不会关联删除
    # null = True：只有NULL才能删除关系
    # related_name = ""
    version = models.ForeignKey("gujianonline.GJOL_Version", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("gujianonline.GJOL_Material_Type", on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey("gujianonline.GJOL_Role",  on_delete=models.SET_NULL, null=True)

    # @staticmethod
    # def version_name(self):
    #     return self.version.short_name

    def get_dict(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        dict_result = {}
        import datetime
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                dict_result[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                dict_result[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                dict_result[attr] = getattr(self, attr)
        return dict_result

    # meta类是配合admin进行管理的
    class Meta:
        db_table = "gjol_material"
        ordering = ["-priority", "sort", "create_time"]  # 默认正序，倒序："-c_time"，"?"来表示随机排序。

        verbose_name = "材料信息表"


# 材料类型表
class GJOL_Material_Type(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, null=False, verbose_name="名称")
    sort = models.SmallIntegerField("排序", max_length=2, default=0)
    remark = models.CharField(max_length=500, verbose_name="备注")
    create_by = models.CharField("创建者", max_length=32, null=False)
    create_time = models.DateTimeField("创建时间", default=timezone.now, null=False)
    update_by = models.CharField("更新者", max_length=32)
    update_time = models.DateTimeField("更新时间")
    is_del = models.BooleanField(default=False)

    class Meta:
        db_table = "gjol_material_type"
        ordering = ["sort", "create_time"]

        verbose_name = "材料类型表"


# 物品信息表
class GJOL_Goods(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField("名称", max_length=40, null=False)
    sort = models.SmallIntegerField("排序", max_length=5, default=99)
    fee = models.DecimalField("加工费", max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField("价格", max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField("描述", max_length=500)
    create_by = models.CharField("创建者", max_length=32, null=False)
    create_time = models.DateTimeField("创建时间", default=timezone.now, null=False)
    update_by = models.CharField("更新者", max_length=32)
    update_time = models.DateTimeField("更新时间")
    is_del = models.BooleanField(default=False)
    # 外键关联
    version = models.ForeignKey("gujianonline.GJOL_Version", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("gujianonline.GJOL_Goods_Type", on_delete=models.SET_NULL, null=True)

    # meta类是配合admin进行管理的
    class Meta:
        db_table = "gjol_goods"
        ordering = ["sort", "create_time"]  # 默认正序，倒序："-c_time"，"?"来表示随机排序。

        verbose_name = "物品信息表"


# 物品类型表
class GJOL_Goods_Type(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField("名称", max_length=40, null=False)
    sort = models.SmallIntegerField("排序", max_length=2, default=0)
    remark = models.CharField("备注", max_length=500)
    create_by = models.CharField("创建者", max_length=32, null=False)
    create_time = models.DateTimeField("创建时间", default=timezone.now, null=False)
    update_by = models.CharField("更新者", max_length=32)
    update_time = models.DateTimeField("更新时间")
    is_del = models.BooleanField(default=False)

    class Meta:
        db_table = "gjol_goods_type"
        ordering = ["sort", "create_time"]

        verbose_name = "物品类型表"


# 物品成分表
class GJOL_Goods_Component(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    # 外键关联
    goods = models.ForeignKey("gujianonline.GJOL_Goods", on_delete=models.SET_NULL, null=True)
    component_type = models.CharField("成品类型", max_length=20)  # material,goods
    component_id = models.CharField("成分ID", max_length=32, null=False)
    component_name = models.CharField("成品名称", max_length=40)
    amount = models.SmallIntegerField("数量", default=1)
    sort = models.SmallIntegerField("排序", default=0)
    create_by = models.CharField("创建者", max_length=32, null=False)
    create_time = models.DateTimeField("创建时间", default=timezone.now, null=False)
    update_by = models.CharField("更新者", max_length=32)
    update_time = models.DateTimeField("更新时间")
    is_del = models.BooleanField(default=False)

    # meta类是配合admin进行管理的
    class Meta:
        db_table = "gjol_goods_component"
        ordering = ["sort", "create_time"]  # 默认正序，倒序："-c_time"，"?"来表示随机排序。

        verbose_name = "物品成分表"


# 版本信息表
class GJOL_Version(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    short_name = models.CharField(max_length=40, null=False, verbose_name="简称")
    start_date = models.DateField(verbose_name="开始日期")
    end_date = models.DateField(verbose_name="结束日期")
    remark = models.CharField(max_length=500, verbose_name="备注")
    create_by = models.CharField("创建者", max_length=32, null=False)
    create_time = models.DateTimeField("创建时间", default=timezone.now, null=False)
    update_by = models.CharField("更新者", max_length=32)
    update_time = models.DateTimeField("更新时间")
    is_del = models.BooleanField(default=False)

    class Meta:
        db_table = "gjol_version"
        ordering = ["start_date", "create_time"]

        verbose_name = "版本信息表"


# 角色信息表
class GJOL_Role(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField("名称", max_length=40, null=False)
    profession = models.CharField("职业", max_length=20, null=False)
    create_date = models.DateField("创建日期")
    sort = models.SmallIntegerField("排序", max_length=2, default=99)
    server_info = models.CharField("区服信息", max_length=100)
    account_info = models.CharField("账号信息", max_length=100)
    remark = models.CharField("备注", max_length=500)
    create_by = models.CharField("创建者", max_length=32, null=False)
    create_time = models.DateTimeField("创建时间", default=timezone.now, null=False)
    update_by = models.CharField("更新者", max_length=32)
    update_time = models.DateTimeField("更新时间")
    is_del = models.BooleanField(default=False)

    class Meta:
        db_table = "gjol_role"
        ordering = ["sort", "create_date", "create_time"]

        verbose_name = "角色信息表"