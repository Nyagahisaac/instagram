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

@login_required(login_url='/accounts/login/')
def home (request):
    title = "Instagram Clone"
    image = Image.objects.all()

    return render(request, 'home.html',{'image': image})

@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            # article.post = strip_tags(request.POST['post'])
            # article.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new-post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user = request.user
    comments =Comment.objects.all()
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
            # article.post = strip_tags(request.POST['post'])
            # article.save()
        return redirect('new_comment')

    else:
        form = NewCommentForm()
    return render(request, 'new-comment.html', {"form": form, "comments": comments})


@login_required(login_url='/accounts/login/')
def search_results(request):
    title="Find"
    images=Image.objects.all()
    
    
    if 'image_name' in request.GET and request.GET['image_name']:
        search_term = request.GET.get('image_name')
        found_results = Image.objects.filter(name__icontains=search_term)
        message = f"{search_term}"


        return render(request, 'search.html',{'title':title,'results': found_results, 'message': message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})