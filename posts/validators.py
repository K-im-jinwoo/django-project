from django.core.exceptions import ValidationError

def validate_symbols(value):
  if ("@" in value) or ("#" in value):
    raise ValidationError("@와 #은 포함될 수 없습니다.", code='symbol-err')

def validate_post_link(value):
  if "map.naver.com" not in value and "place.map.kakao.com" not in value:
    raise ValidationError("네이버, 카카오 링크가 들어가야 합니다.")