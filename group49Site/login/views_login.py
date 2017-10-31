from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render_to_response, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def loginPageView(request):

    context = {'error':""}
    return render(request, 'login.html', context)

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
        request.session['user_type']= user.user_type
        return redirect("/accounts/profile")
    else:
        context = { 'error': "Incorrect User or Password"}
        return render(request,"login.html", context)



def logout_view(request):
    logout(request)
    return redirect("/login")









