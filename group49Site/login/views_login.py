from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm



def loginPageView(request):

    template = loader.get_template('login.html')

    return HttpResponse(template.render({},request))

def registerPageView(request):

    template = loader.get_template('register.html')

    return HttpResponse(template.render({},request))


def registration_complete(request):
     return render_to_response('registration_complete.html')