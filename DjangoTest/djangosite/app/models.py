from django.db import models


KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('数据库技术', '数据库技术'),
    ('其他', '其他'),
)


class Moment(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])