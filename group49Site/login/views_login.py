from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from introduction_page.models import userRegisterAccount


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

    user = get_user_model()
    password_check = user.objects.raw("SELECT id, password FROM auth_user WHERE username = '" +
                                      username + "'")[0].password

    print(password_check)
    if(password == password_check):
        print("access granted")
        return
    else:
        print("access denied")
    return HttpResponse('swas')





