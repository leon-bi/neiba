from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site= models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted =models.DateTimeField(default=timezone.now)    
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Neibour',blank=True)


