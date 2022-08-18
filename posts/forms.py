from django import forms
from .models import Post, Review
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    
  class Meta:
    model = Post
    fields = ['title', 'content']

  def clean_title(self):
    title = self.cleaned_data['title']
    if '*' in title:
      raise ValidationError('*는 포함될 수 없습니다.')

    return title

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ['title', 'content', 'post_link', 'rating', 'image1', 'image2', 'image3']
    widgets = {
      "rating": forms.RadioSelect,
    }