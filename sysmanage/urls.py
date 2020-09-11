from django.urls import path  # 处理接口方法
from sysmanage import views  # 后台处理
from django.conf import settings  # 全局设置
from django.conf.urls.static import static  # 静态文件

urlpatterns = [
                  path('index', views.index, name='index'),  # 首页
                  path('menu_page', views.menu_page),  # 菜单页面
                  path('menu_data', views.menu_data),  # 菜单数据
                  path('menu_add', views.menu_add),  # 菜单新增
                  path('menu_del', views.menu_del),  # 菜单删除
                  path('check_theme', views.check_theme),  # 修改主题
                  path('menu_edit', views.menu_edit),  # 菜单编辑
                  path('menu_info', views.menu_info),  # 菜单详情
                  path('menu_list_left_tree', views.menu_list_left_tree),  # 菜单管理左侧树
                  path('menu_add_parent_tree', views.menu_add_parent_tree),  # 菜单新增上级id树
                  path('user_page', views.user_page),  # 用户页面
                  path('user_data', views.user_data),  # 用户数据
                  path('user_add', views.user_add),  # 用户添加
                  path('user_del', views.user_del),  # 用户删除
                  path('user_edit', views.user_edit),  # 用户编辑
                  path('user_check_password', views.user_check_password),  # 用户修改密码
                  path('user_info', views.user_info),  # 用户详情
                  path('add_browse_record', views.add_browse_record),  # 添加浏览数据
                  path('select_browse_record', views.select_browse_record),  # 查询浏览记录
                  path('online_page', views.online_page),  # 上线页面
                  path('online_data', views.online_data),  # 上线数据
                  path('online_quit_it', views.online_quit_it),
                  path('role_page', views.role_page),  # 角色页面
                  path('role_data', views.role_data),  # 角色数据
                  path('role_menu_manage', views.role_menu_manage),  # 角色菜单管理树
                  path('generate_page', views.generate_page),  # 页面
                  path('generate_data', views.generate_data),  # 数据
                  path('generate_info', views.generate_info),  # 查看
                  path('file_generate', views.file_generate),  # 文件生成
                  path('file_download', views.file_download),  # 文件下载
                  path('icon_list', views.icon_list),  # icon图表列表
                  path('check_icon', views.check_icon),  # 选择icon
                  path('sublime_test', views.sublime_test),  # 代码生成普通
                  path('test', views.test),  # 代码生成普通
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
