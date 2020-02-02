from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,CreateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from testapp.forms import PostForm
from django.http import HttpResponse
from .models import Student
# Create your views here.


class HomePage(TemplateView):
    template_name = 'index.html'



def index(request):
    print(request.method)

    if request.method=='POST':
        full_name = request.POST.get('fname')
        email = request.POST.get('email')
        gname = request.POST.get('gname')

        s = Student(name=full_name,email=email)

        s.save()

    return render(request,'testapp/index.html')
