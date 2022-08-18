from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import (
  ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse
from .models import Post, Review
from .forms import PostForm, ReviewForm

# Create your views here.

def index(request):
  return render(request, 'posts/index.html')

def post_list(request):
  post = Post.objects.all()
  context = {'post':post}
  return render(request, 'posts/post_list.html', context)

def post_detail(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  context = {'post': post}
  return render(request, 'posts/post_detail.html', context)

def post_create(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      new_post = post_form.save()
      return redirect('post-detail', post_id=new_post.id)
  else:
    post_form = PostForm()
  return render(request, 'posts/post_form.html', {'form': post_form})

def post_update(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == 'POST':
    post_form = PostForm(request.POST, instance=post)
    if post_form.is_valid():
      post_form.save()
      return redirect('post-detail', post_id=post.id)
      
  else:
    post_form = PostForm(instance=post)
  return render(request, 'posts/post_form.html', {'form': post_form})
    

def post_delete(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == 'POST':
    post.delete()
    return redirect('post-list')
  else:
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

# 리뷰
class ReviewListView(ListView):
  model = Review
  template_name = "posts_review/review_list.html"
  context_object_name = "reviews"
  paginate_by = 4
  ordering = ["-dt_created"]

class ReviewDetailView(DetailView):
  model = Review
  template_name = "posts_review/review_detail.html"
  pk_url_kwarg = "review_id"

class ReviewCreateView(CreateView):
  model = Review
  form_class = ReviewForm
  template_name = "posts_review/review_form.html"

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def get_success_url(self):
    return reverse("review-detail", kwargs={"review_id": self.object.id})

class ReviewUpdateView(UpdateView):
  model = Review
  form_class = ReviewForm
  template_name = "posts_review/review_form.html"
  pk_url_kwarg = "review_id"

  def get_success_url(self):
    return reverse("review-detail", kwargs={"review_id": self.object.id})

class ReviewDeleteView(DeleteView):
  model = Review
  template_name = "posts/post_confirm_delete.html"
  pk_url_kwarg = "review_id"

  def get_success_url(self):
    return reverse("review-list")