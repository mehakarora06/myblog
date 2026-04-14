from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import SignupForm, PostForm


# 🏠 HOME (Public - anyone can see)
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


# 🔐 SIGNUP
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


# ✍️ CREATE POST
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   # 🔥 IMPORTANT FIX
            post.save()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


# ✏️ EDIT POST
@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    # 🔒 Only author can edit
    if post.author != request.user:
        return redirect('/')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})


# 🗑️ DELETE POST
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    # 🔒 Only author can delete
    if post.author != request.user:
        return redirect('/')

    post.delete()
    return redirect('/')