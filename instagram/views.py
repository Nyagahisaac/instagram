from django.http.response import HttpResponse
from django.shortcuts import  render ,redirect, get_object_or_404
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .emails import send_welcome_email
from .models import Image,Profile,Comment
from .forms import NewImageForm, NewCommentForm, NewProfileForm
from django.contrib import messages


# Create your views here.
User = get_user_model

@login_required()
def home (request):
    title = "Instagram Clone"
    image = Image.objects.all()

    return render(request, 'home.html',{'image': image})

@login_required()
def profile(request):
    title = 'My-Profile'

    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('profile')

        else:
            form = NewProfileForm()
        user=current_user
        profile =Profile.get_profile(user)
        return render(request, 'profile.html', {'profile': profile, 'title': title, 'form': form})