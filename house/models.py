from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name = '用户表'
        db_table = 'user'

    username = models.CharField('用户名', max_length=20)  # 用户名/手机号
    password = models.CharField('密码', max_length=20)  # 密码
    rentorsell = models.BooleanField('用户类型', default=False)  # 0 rent 1 sell
    gender_choice = (
        ('male', '男'),
        ('female', "女")
    )
    gender = models.CharField('性别', max_length=6, choices=gender_choice)  # 性别
    identifyid = models.CharField('身份证', max_length=18)  # 身份证 18位
    address = models.CharField('邮箱地址', max_length=30)  # 邮箱地址
    email = models.CharField('邮箱', max_length=20)  # email邮件
    phone = models.CharField('电话', max_length=11)  # 联系电话


class houseintro(models.Model):
    class Meta:
        verbose_name = '房屋信息表'
        db_table = 'houseintro'

    house_name = models.CharField('此小区名称', max_length=50)
    house_type = models.CharField('户型', max_length=20)
    house_size = models.CharField('平米数', max_length=8)
    house_high_message1 = models.CharField('共几层', max_length=3)
    house_high_message2 = models.CharField('第几层', max_length=3)
    house_rent_money = models.CharField('租金/每月', max_length=10)
    house_facility = models.CharField('设施简介', max_length=500)
    house_renter_phone = models.CharField('联系方式', max_length=11)
    img_url = models.ImageField(upload_to='images')
    house_ts=models.CharField('特色',max_length=100,null=True)
