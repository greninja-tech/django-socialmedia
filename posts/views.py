from django.shortcuts import render,redirect,get_object_or_404
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Post, Comment
# Create your views here.

def addpost(request):
    if request.method=="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})

def myposts(request):
    posts = Post.objects.filter(user=request.user)
    return render(request,'posts/my_posts.html',{'posts':posts})

def otherposts(request):
    posts = Post.objects.all().exclude(user=request.user)
    return render(request,'posts/other_posts.html',{'posts':posts})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, user=request.user, content=content)
    return redirect(request.META.get('HTTP_REFERER', 'home'))
