from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100, unique=True, error_messages={'unique': '이미 있는 제목입니다.'})
  content = models.TextField(validators=[MinLengthValidator(10, '너무 짧습니다. 10자 이상 적어주세요.'), validate_symbols])
  dt_created = models.DateTimeField(auto_now_add=True)
  dt_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title