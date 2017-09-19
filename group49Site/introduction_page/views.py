
from django.shortcuts import HttpResponse
from django.template import loader



def homePageView(request):

    template = loader.get_template('base.html')

    return HttpResponse(template.render({},request))


def aboutPageView(request):

    template = loader.get_template('about.html')

    return HttpResponse(template.render({},request))







