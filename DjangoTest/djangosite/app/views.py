from django.http import HttpResponse
import os
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("<h1>Welcome to my site.</h1>")


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    return render(request, os.path.join(PROJECT_ROOT, 'templates', 'moments_input.html'), {'form': form})