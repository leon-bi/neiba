from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted =models.DateTimeField(default=timezone.now)    
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Neibour',blank=True)
    objects=models.Manager()

    def __str__(self):
        return self.title 
    
    @classmethod
    def search_by_title(cls,search_term):
        post= cls.objects.filter(title__icontains=search_term)
        return post



    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        

class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants = models.IntegerField(auto_created=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('neiba-detail', kwargs={'pk': self.pk})


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('business-detail', kwargs={'pk': self.pk})
