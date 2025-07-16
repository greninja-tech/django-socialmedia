from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to='post_images/',blank=True,null=True)
    created_at=models.DateTimeField(default=timezone.now)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_posts',blank=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
