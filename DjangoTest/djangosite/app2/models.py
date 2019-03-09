from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10, null=False, verbose_name="名字")
    age = models.IntegerField(null=False, verbose_name="年龄")

    class Meta:
        db_table = 'User'
        verbose_name = "用户"

    def __str__(self):
        return self.name

