from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    #override get context data method 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['books'] = Bookshelf.objects.all()
        context['more'] = More.objects.all()
        return context