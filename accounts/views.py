from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import RegistrationForm,loginform
from accounts.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from django.shortcuts import redirect,get_object_or_404
from posts.models import Post
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.is_active=True
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email, password=password)

            if user is not None:
                if not user.is_active:
                    messages.error(request, 'Account is inactive.')
                else:
                    login(request, user)
                    messages.success(request, 'Your login has been successful')
                    return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        form = loginform()

    return render(request, 'accounts/login.html', {'form': form})


def profile_view(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=profile_user)

    is_following = False
    if profile_user != request.user:
        is_following = profile_user in request.user.following.all()

    return render(request, 'accounts/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'is_following': is_following,
    })
def toggle_follow(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if target_user == request.user:
        return redirect('profile', user_id=user_id)

    if target_user in request.user.following.all():
        request.user.following.remove(target_user)
    else:
        request.user.following.add(target_user)

    return redirect('profile', user_id=user_id)

def logout_view(request):
    logout(request)
    return redirect('login')
    



