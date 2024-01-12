from django.shortcuts import render, redirect

# Create your views here.

from .sign_up_form import sign_up

from django.contrib import messages


def sign_up_page(request):
    if not request.user.is_authenticated:
            
        if request.method == "POST":
            form = sign_up(request.POST)
            if(form.is_valid()):
                messages.success(request, 'Account create successfully')
                form.save()
                return redirect('login')

        else:
            form = sign_up()
        return render(request, 'signUp.html', {"form": form})
    else:
        return redirect('profile')



def homepage(request):
    return render(request, 'homepage.html')



from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login, logout


def userLogin(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                userName = form.cleaned_data['username']
                userPassword = form.cleaned_data['password']
                user = authenticate(username = userName, password = userPassword)

                if user is not None:
                    login(request,user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    else:
        return redirect('profile')



def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {"user": request.user})
    else:
        return redirect('login')


def userLogout(request):
    logout(request)
    return redirect("login")



from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from django.contrib.auth import update_session_auth_hash

def changePasswordWithOldPassword(request):
    if request.user.is_authenticated:
        # return redirect("login") # TODO go to login page redirect
        if request.method == "POST":
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'passwordChange.html',{'form':form})
    
    else:
        return redirect('login')
    

        

def changePasswordWithOutOldPassword(request):
    if not request.user.is_authenticated:
        return redirect('login') # thats will be return login page if user is not authenticated

    else:
        if request.method == "POST":
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                return redirect('login')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, 'passwordChange.html', {'form':form})

from firstApp.sign_up_form import sign_up
from .editProfile import EditProfile

def EditProfileInfo(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":
            form =EditProfile(request.POST, instance = request.user)
            if(form.is_valid()):
                form.save()
                return redirect('profile')

        else:
            form = EditProfile(instance= request.user)

        return render(request, 'signUp.html', {"form": form})
    else:
        return redirect('login')
    

def showProfile(request):
        if request.user.is_authenticated:
            # data = request.user.objects.all()
            return render(request, 'showProfileData.html')
        return redirect('login')




