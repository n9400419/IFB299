
from django.shortcuts import HttpResponse, render
from django.template import loader



def homePageView(request):

   return render(request, 'base.html')


def aboutPageView(request):

    return render(request, 'about.html')






