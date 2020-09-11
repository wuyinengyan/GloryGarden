from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from loginmanage.views import log_in
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.paginator import Paginator  # Django内置分页功能模块
from gujianonline.models import *
from django.http import JsonResponse
# from loginmanage.util import *  # 自定义工具类
from django.db.models import F,Q
# from GloryGarden.common import *


# 默认日期
def set_default_date(date):
    if(not len(date)):
        date = "0001-01-01"
    return date