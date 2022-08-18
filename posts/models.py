from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols, validate_post_link
from user.models import User

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100, unique=True, error_messages={'unique': '이미 있는 제목입니다.'})
  content = models.TextField(validators=[MinLengthValidator(10, '너무 짧습니다. 10자 이상 적어주세요.'), validate_symbols])
  dt_created = models.DateTimeField(auto_now_add=True)
  dt_modified = models.DateTimeField(auto_now=True)

  author = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.title

class Review(Post):
  post_link = models.URLField(validators=[validate_post_link])

  RATING_CHOICES = [
    (1,"★"),
    (2,"★★"),
    (3,"★★★"),
    (4,"★★★★"),
    (5,"★★★★★"),
  ]
  rating = models.IntegerField(choices=RATING_CHOICES, default=None)

  image1 = models.ImageField(upload_to="review_pics")
  image2 = models.ImageField(upload_to="review_pics", blank=True)
  image3 = models.ImageField(upload_to="review_pics", blank=True)


  def __str__(self):
    return self.title
