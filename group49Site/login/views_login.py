from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login



def loginPageView(request):

    template = loader.get_template('login.html')

    return HttpResponse(template.render({},request))

def registerPageView(request):

    template = loader.get_template('register.html')

    return HttpResponse(template.render({},request))


def registration_complete(request):
     return render_to_response('registration_complete.html')


def submit_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")

    return redirect("/login")     











