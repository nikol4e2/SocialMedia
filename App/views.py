from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from App.models import Profile


# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"User with that email already exists!")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken!")
                return  redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request,"Passwords do not match!")

    else:
        return render(request, 'signup.html')
