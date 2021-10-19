from django.http.response import HttpResponse
from django.shortcuts import  render ,redirect, get_object_or_404
import datetime as dt
from .models import Profile,Image,User
from django.contrib.auth import get_user_model,login,logout
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from .forms import NewImageForm, NewCommentForm, NewProfileForm 
from django.contrib import messages
from .emails import send_register_welcome_email


# Create your views here.
User = get_user_model

@login_required
def home (request):
    title = "Instagram Clone"
    image = Image.objects.all()

    return render(request, 'home.html',{'image': image})

def register(request):
    '''
    this is a view function that is responsible for rendering our register form and funtionality
    '''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password =request.POST['confirm_password']
        
        if confirm_password == password:
            if User.objects.filter(username = username):
                messages.info(request,'This username is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,email = email,password = password,confirm_password = confirm_password)
                user.save()
                send_register_welcome_email(username,email)
                return redirect('home')
        else:
            messages.info(request,'passwords should match')
            return redirect('register')
        
    else:
        return render(request,'registration/registration_form.html')
    

def logout_view(request):
    logout(request)
    return redirect('/')
# def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('edit-profile')
    else:
        form = SignupForm()
    
    context = {
        'form':form,
    }

    return render(request, 'home.html', context)


@login_required
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


@login_required
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
    return render(request, 'comments.html', {"form": form, "comments": comments})


@login_required
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