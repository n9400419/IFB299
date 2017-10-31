from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .accounts_form import SignUpForm
from .models import User
from search.models import Hotel, College, Industry, Library, Zoo, Museum, Restaurant, Mall, Park

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
        #    user.UserType.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.first_name = form.cleaned_data.get('first_name')
            #user.user_type = request.POST['user_type']
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')


            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Success')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def profile_view(request):

    return render(request,'profile.html')

def success_view(request):

    return render(request,'register_complete.html')

def hotel_view(request):
    results = Hotel.objects.all()[:5]
    context = {'results':results}
    return render(request, 'profile.html', context)

def college_view(request):
    results = College.objects.all()[:5]
    context = {'results':results}
    return render(request, 'profile.html', context)

def library_view(request):
    results = Library.objects.all()[:5]
    context = {'results':results}
    return render(request, 'profile.html', context)


def industry_view(request):
    results = Industry.objects.all()[:5]
    context = {'results':results}
    return render(request, 'profile.html', context)

def citymap_view(request):

    return render(request,'citymap.html')

def cityinformation_view(request):

    return render(request,'cityinformation.html')

def zoos_view(request) :
    results = Zoo.objects.all()[:5]
    context = {'results':results}
    return render(request, 'cityinformation.html', context)


def malls_view(request) :
    results = Mall.objects.all()[:5]
    context = {'results':results}
    return render(request, 'cityinformation.html', context)

def museums_view(request) :
    results = Museum.objects.all()[:5]
    context = {'results':results}
    return render(request, 'cityinformation.html', context)

def restaurants_view(request) :
    results = Restaurant.objects.all()[:5]
    context = {'results':results}
    return render(request, 'cityinformation.html', context)


def parks_view(request) :
    results = Park.objects.all()[:5]
    context = {'results':results}
    return render(request, 'cityinformation.html', context)


def request_access_view(request):
    return render(request, 'requestaccess.html')







