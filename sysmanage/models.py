from django.db import models
from mptt.models import MPTTModel
import django.utils.timezone as timezone
import uuid


# 菜单
class Menu(MPTTModel):
    name = models.CharField('名称', max_length=50, unique=True)
    menu_url = models.CharField(max_length=255, blank=True, null=True)
    menu_order = models.CharField(max_length=100, blank=True, null=True)
    menu_icon = models.CharField(max_length=60, blank=True, null=True)
    menu_type = models.CharField(max_length=10, blank=True, null=True)
    menu_state = models.IntegerField(blank=True, null=True)
    attributes_color_type = models.CharField(max_length=30, blank=True, null=True)
    attributes_other = models.CharField(max_length=100, blank=True, null=True)
    shiro_key = models.CharField(max_length=100, blank=True, null=True)
    menu_states = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField('是否使用', blank=True, null=True, default=1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='上级菜单', null=True, blank=True,
                               related_name='children')

    class Meta:
        db_table = 'sys_menu'
        verbose_name = verbose_name_plural = '菜单管理'

    class MPTTMeta:
        parent_attr = 'parent'

    def __str__(self):
        return self.name


# 角色
class Role(models.Model):
    role_id = models.CharField(primary_key=True, default=uuid.uuid4(), verbose_name=u'app uuid', max_length=50,
                               help_text="app uuid")
    role_name = models.CharField('角色名称', max_length=30)
    role_menu_rights = models.CharField('角色菜单权限', max_length=255, blank=True, null=True, )
    role_create_rights = models.CharField('角色新增权限', max_length=255, blank=True, null=True, )
    role_delete_rights = models.CharField('角色删除权限', max_length=255, blank=True, null=True, )
    role_update_rights = models.CharField('角色修改权限', max_length=255, blank=True, null=True, )
    role_select_rights = models.CharField('角色查看权限', max_length=255, blank=True, null=True, )
    role_order = models.CharField('角色排序', max_length=30)
    is_active = models.IntegerField('是否使用', blank=True, null=True, default=1)

    class Meta:
        db_table = 'sys_role'

    def __str__(self):
        return self.role_name


# 用户
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user_full_name = models.CharField('用户名', max_length=30, null=True, blank=True, )
    user_name = models.CharField('账号', max_length=30)
    user_password = models.CharField('密码', max_length=30)
    user_email = models.CharField('邮箱', max_length=45, null=True, blank=True)
    user_sex = models.IntegerField('性别')
    user_phone_number = models.CharField('电话号码', null=True, blank=True, max_length=20, )
    user_card = models.CharField('身份证号码', max_length=30)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    createby = models.CharField('创建者', max_length=32)
    createtime = models.DateTimeField('创建时间', default=timezone.now)
    updateby = models.CharField('更新者', max_length=32, null=True)
    updatetime = models.DateTimeField('更新时间', blank=True, null=True)
    is_active = models.IntegerField('是否使用', blank=True, null=True, default=1)
    img_url = models.ImageField('头像', upload_to='img', blank=True, null=True)
    # theme = models.CharField('用户名', max_length=30, null=True, blank=True, )

    class Meta:
        db_table = 'sys_user'

    def get_id(self):
        return self.id


# 浏览记录
class Browse_record(models.Model):
    browse_id = models.AutoField(primary_key=True, editable=False)
    user_id = models.UUIDField(blank=True, null=True)
    menu_id = models.IntegerField('菜单名称', blank=True, null=True)
    createby = models.DateTimeField('保存日期', default=timezone.now)

    class Meta:
        db_table = 'sys_browse_record'

        # 注意！这里必须重写，因为源码使用unicode(id)，但是python3没有unicode()方法！此时就无法登录用户！

    def get_id(self):
        return self.user_id


# 在线情况
class Online(models.Model):
    online_id = models.AutoField(primary_key=True, )
    user_id = models.CharField('用户名', max_length=255)
    online_date = models.DateTimeField('上线日期', default=timezone.now)

    class Meta:
        db_table = 'sys_online'

    def get_id(self):
        return self.user_id


# 数据字典
class Dictionary(models.Model):
    dict_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    dict_name = models.CharField('类型名称', max_length=255)
    dict_cont = models.CharField('分类内容', max_length=255)
    dict_class = models.CharField('分类名称', max_length=255)
    dict_order = models.IntegerField('字段顺序', null=True)
    parent_id = models.CharField('pid', max_length=255)
    createtime = models.DateTimeField('创建时间', default=timezone.now)
    update_date = models.DateTimeField('修改时间', default=timezone.now)
    is_active = models.IntegerField('是否使用', default=1)
    dict_type = models.IntegerField('字典类型')



    class Meta:
        db_table = 'sys_dictionary'

    def get_id(self):
        return self.dict_name


class Test(models.Model):
    img_name = models.CharField('类型名称', max_length=255, blank=True, null=True)
    img_url = models.ImageField(upload_to='img')  # upload_to指定图片上传的途径，如果不存在则自动创建

    class Meta:
        db_table = 'sys_Test'

    def get_id(self):
        return self.img_url


class Generate(models.Model):
    generate_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField('名称', max_length=255)
    is_active = models.IntegerField('是否使用', default=1)
    class Meta:
        db_table = 'sys_generate'

    def get_id(self):
        return self.generate_id
