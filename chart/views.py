from django.shortcuts import render
from .models import Country
from django.views import View
from .models import Country

# Create your views here.

class Home(View):
    def get (self, request,*args,**kwargs):
        pp = Country.objects.all()
        context = {'pp':pp}
        return render (request, 'home.html', context)