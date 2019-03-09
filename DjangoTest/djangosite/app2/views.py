from django.shortcuts import render
from django.http import HttpResponse
from app2 import models


def users(request):
    user = models.User()
    user.name = "名称1"
    user.age = 18
    user.save()
    user = models.User()
    user.name = "名称2"
    user.age = 21
    user.save()
    models.User.objects.create(name="名称3", age=22)
    return HttpResponse("执行完成")
