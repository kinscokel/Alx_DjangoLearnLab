from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
        messages.success(request, 'Profile updated.')
    return render(request, 'registration/profile.html')


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Create templates/home.


# blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# List all posts, accessible to all users
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

# Detail view for a post, accessible to all users
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create a post, only for authenticated users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update post, only author can update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete post, only author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/comments/add_comment.html', {'form': form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('post_detail', pk=comment.post.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully.')
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comments/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post
    if request.user != comment.author:
        return redirect('post_detail', pk=post.id)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('post_detail', pk=post.id)
    return render(request, 'blog/comments/delete_comment.html', {'comment': comment})


from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Comment, Post
from .forms import CommentForm

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comments/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comments/edit_comment.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comments/delete_comment.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})

from django.shortcuts import render
from django.db.models import Q
from .models import Post

def search_posts(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})



from django.shortcuts import get_object_or_404
from taggit.models import Tag

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__slug=tag_slug)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag_name': tag.name})

