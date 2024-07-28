from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from gmsapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(req):
    return render(req,"HomePage.html")
@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/')
def user_login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(req, user)
            print("Successfully Logged in")
            return HttpResponseRedirect('/')  # Redirect to your dashboard or another page after successful login
        else:
            print('Login Failed')

    return render(req, "LoginPage.html")

def signup(req):
    registered = False

    if req.method == 'POST':
        user_form = UserForm(req.POST)
        profile_form = UserProfileInfoForm(req.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print('Error in user registration')
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(req, "SignupPage.html", {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})