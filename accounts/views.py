from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage

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
    current_user = request.user
    
    if not current_user.is_superuser:
        profile = Profile.objects.get_or_create(user=current_user)       
        if request.method == "POST":
            fullname        =request.POST['fullname']
            country         =request.POST['Country']
            streetaddress   = request.POST['address']
            city            = request.POST['city']
            postcode        = request.POST['zipcode']
            phone           = request.POST['phone']
            email           = request.POST['email']
            image           = request.FILES['pimage']
            if image:
                profileimg = FileSystemStorage().save('profile/' + image.name, image)
                profile[0].image  = profileimg
            profile[0].full_name  = fullname
            profile[0].country    = country
            profile[0].address    = streetaddress
            profile[0].city       = city
            profile[0].zipcode    = postcode
            profile[0].phone      = phone
            profile[0].email      = email
            profile[0].save()
        
        mycontext = {
                'profile': profile[0],
            }
        return render(request, "accounts/profile.html",mycontext)
        
        
    
