from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Topic , Message
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.


def loginPage(request):
    page = 'loginpage'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error in authentication')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def registerPage(request):
    page = 'registerpage'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.usename = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "ERROR in Authentication")

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts1 = Post.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    post_count = posts1.count()

    context = {'posts1': posts1, 'topics': topics, 'post_count': post_count}

    return render(request, 'base\home.html', context)


def posts(request, pk):
    post = Post.objects.get(id=pk)
    postmessages = post.message_set.all().order_by('-created')
    
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('body')

        )
        return redirect('posts', pk = post.id)
    
    
  
    
    context = {'post': post, 
            'postmessages' : postmessages}
    return render(request, 'base\posts.html', context)


@login_required(login_url='loginpage')
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url='loginpage')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    context = {'form': form}

    if request.user != post.host:
        return HttpResponse("No access for you for thia page")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/post_form.html', context)


@login_required(login_url='loginpage')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.host:
        return HttpResponse("No access for you for thia page")

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': post})


def logoutUser(request):
    logout(request)
    return redirect('home')
