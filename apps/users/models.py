# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    companyName = models.CharField(verbose_name=u"公司名称", max_length=50)
    addTime = models.DateField(verbose_name=u"注册时间", blank=True, null=True)
    mobileNumber = models.CharField(verbose_name=u"手机号码", default="110",
                                    max_length=11)
    userType = models.CharField(verbose_name=u"用户类别",
                                choices=(("student", u"学生"),
                                         ("teacher", u"教师")),
                                default="student", max_length=20)
    grade = models.CharField(verbose_name=u"成绩", default="100", max_length=50)
    userImage = models.ImageField(upload_to="image/%Y/%m",
                                  default="image/default.png")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="Banner/%Y/%m", verbose_name=u"轮播图",
                              max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
