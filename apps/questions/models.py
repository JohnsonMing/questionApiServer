# _*_ encoding: utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.
class LegalSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"法制安全问题"
        verbose_name_plural = verbose_name


class FireSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"消防安全问题"
        verbose_name_plural = verbose_name


class MentalHealthSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"心理健康安全问题"
        verbose_name_plural = verbose_name


class TrafficSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"交通安全问题"
        verbose_name_plural = verbose_name


class PersonalSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"人身财产安全问题"
        verbose_name_plural = verbose_name


class ActivityStudySecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"学习活动安全问题"
        verbose_name_plural = verbose_name


class FoodSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"食品安全问题"
        verbose_name_plural = verbose_name


class NationalSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"国家安全问题"
        verbose_name_plural = verbose_name


class NetworkSecurity(models.Model):
    questionType = models.CharField(max_length=10, verbose_name=u"问题类型")
    questionNumber = models.CharField(max_length=10, verbose_name=u"问题序号")
    questionContent = models.CharField(max_length=100, verbose_name=u"问题内容")
    AnswerA = models.CharField(max_length=50, verbose_name=u"答案A")
    AnswerB = models.CharField(max_length=50, verbose_name=u"答案B")
    AnswerC = models.CharField(max_length=50, verbose_name=u"答案C", null=True, blank=True)
    AnswerD = models.CharField(max_length=50, verbose_name=u"答案D", null=True, blank=True)
    AnswerE = models.CharField(max_length=50, verbose_name=u"答案E", null=True, blank=True)
    AnswerF = models.CharField(max_length=50, verbose_name=u"答案F", null=True, blank=True)
    AnswerG = models.CharField(max_length=50, verbose_name=u"答案G", null=True, blank=True)
    AnswerH = models.CharField(max_length=50, verbose_name=u"答案H", null=True, blank=True)
    RightAnswer = models.CharField(max_length=50, verbose_name=u"正确答案", default="A")
    questionScore = models.CharField(verbose_name=u"分值", max_length=5, default="2")
    addTime = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"网络安全问题"
        verbose_name_plural = verbose_name
