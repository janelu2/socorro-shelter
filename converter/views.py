from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    return render(request, 'converter/index.html')

def about(request):
    return render(request, 'converter/about.html')

def services(request):
    return render(request, 'converter/services.html')

def contact(request):
    return render(request, 'converter/contact.html')

def lost(request):
    return render(request, 'converter/lost.html')

def faq(request):
    return render(request, 'converter/faq.html')

def donate(request):
    return render(request, 'converter/donate.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'converter/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'converter/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'converter/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'converter/post_edit.html', {'form': form})
