from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('posts/', views.post_list, name='post-list'),
path('posts/new/', views.post_create, name='post-create'),
path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
path('posts/<int:post_id>/edit/', views.post_update, name='post-update'),
path('posts/<int:post_id>/delete/', views.post_delete, name='post-delete'),
# 리뷰
path("reviews/", views.ReviewListView.as_view(), name="review-list"),
path("reviews/<int:review_id>/", views.ReviewDetailView.as_view(), name="review-detail"),
path("reviews/new/", views.ReviewCreateView.as_view(), name="review-create"),
path("reviews/<int:review_id>/edit/", views.ReviewUpdateView.as_view(), name="review-update"),
path("reviews/<int:review_id>/delete/", views.ReviewDeleteView.as_view(), name="review-delete")
]