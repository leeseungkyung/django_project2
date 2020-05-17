from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    image_thumbnail = ImageSpecField(source='image',
                      processors=[Thumbnail(400, 400)],
                      format='JPEG',
                      options={'quality': 60})
    image = models.ImageField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)