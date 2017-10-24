from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .accounts_form import SignUpForm
from .models import User
from search.models import Hotel, College, Industry, Library

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
        #    user.UserType.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.first_name = form.cleaned_data.get('first_name')

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')


            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def profile_view(request):

    return render(request,'profile.html')

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















