#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import xadmin
from .models import Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "安全知识问答后台管理系统"
    site_footer = "浙江水利水电学院"
    menu_style = "accordion"


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
