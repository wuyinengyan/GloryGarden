# hRoot

#### 介绍
{**以下是码云平台说明，您可以替换此简介**
码云是 OSCHINA 推出的基于 Git 的代码托管平台（同时支持 SVN）。专为开发者提供稳定、高效、安全的云端软件开发协作平台
无论是个人、团队、或是企业，都能够用码云实现代码托管、项目管理、协作开发。企业项目请看 [https://gitee.com/enterprises](https://gitee.com/enterprises)}

#### 软件架构
软件架构说明

#### 安装教程

环境&技术栈  
#####

 python3  
 django   
 django-mptt  
 git  
 gitee  
 layui  
 jquery  
 ztree  
 

## 切记--- 用这个仓库 mydevelop ！！！
1.打开pycharm 选择git clone 项目，如果之前没有登录没有安装gitee-plugin请百度或者容我慢慢道来

![pycharm_git](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%88%E8%8E%B7%E5%8F%96%E9%A1%B9%E7%9B%AE%EF%BC%89.png)

2.运行
 ```
 python3 manage.py runserver
 ```
![运行](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%88%E8%B7%91%E9%A1%B9%E7%9B%AE%EF%BC%89.png)

3.看一下有没有报错
    
>一般会出现的错误
>>1.编码需要转换成encode 链接：https://www.jianshu.com/p/96a244db240f  
>>2.mysqlclient版本需要更新  https://www.jianshu.com/p/defb8bae92f1  
>>3.如果报错mptt 不存在，执行  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django-mptt    
>>4.runserver时候 AttributeError错误， 'utf-8' codec can。。。  https://www.jianshu.com/p/537215f666cb  
>>5.如果pycharm没设置，debug或者run（右上角的）会报错 manage.py不是32位有效程序  
>>6.其他就是环境或者项目需要的包没有安装，此处不赘述了  

4.数据库文件  
    1.sql文件:hRoot/static/data/entmanage.sql  
    2.插入语句:hRoot/static/data/insert_data

#### 使用说明

 title  | code  |
 :----: | :-----: |  
 创建数据库  | python3 manage.py migrate |
 让 Django 知道我们在我们的模型有一些变更  | python3 manage.py makemigrations |
 让项目跑起来（后面可以加端口号）  | python3 manage.py runserver  |
 根据数据库生成model|python3 manage.py inspectdb|
 创建项目|django-admin startproject ...|
 创建app|python3 manage.py startapp ...|
 查看具体的错误 | python manage.py test -v3 sitecoming|  



#### 系统展示


#####登录页面
![登录页面](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/show_login.png)
#####首页
![首页](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/show_index.png)
#####菜单管理页面
![菜单管理页面](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/show_menu.png)
#####角色管理页面
![角色管理页面](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/show_role.png)
#####角色管理新增页面
![角色管理新增页面](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/show_role_b_add.png)
#####用户管理
![用户管理](https://gitee.com/btdba/hRoot/raw/mydevelop/static/readme_img/show_user.png)


#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)