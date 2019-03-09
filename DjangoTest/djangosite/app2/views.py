from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app2 import models
from django.core.urlresolvers import reverse
from app2.forms import UserForm


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


def year(request, year):
    return render(request, 'render.html', {'year': year, })


def year2(request):
    return HttpResponseRedirect(reverse('when', args=['1998']))


def formtest(request):
    form = UserForm()
    return render(request, 'render.html', {'user': form})


def hello(request):
    form = UserForm(request.POST)
    if form.is_valid():
        return HttpResponse("Hello World!!!")
    else:
        return HttpResponse("Error")
