from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required


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
 
@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
from django.shortcuts import get_object_or_404

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    post.delete()
    return redirect('/')