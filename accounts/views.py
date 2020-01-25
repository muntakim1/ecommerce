from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user is not user.is_superuser:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid user name or Password')
        else:
            messages.error(request, 'Invalid user name or Password')

    form = AuthenticationForm()

    return render(request, "accounts/login.html", context={'form': form})
def register_view(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
 
    else:
        f = UserCreationForm()
 
    return render(request, 'accounts/register.html', {'form': f})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('/')


def profile_view(request):
    
    profile = Profile.objects.all()
    
    mycontext = {
        'profile': profile,
        
    }
    return render(request, "accounts/profile.html", mycontext)
