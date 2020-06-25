from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return '%s' %(self.user.first_name)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.IntegerField()
    msg = models.TextField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)

class Playlist(models.Model):
    title = models.CharField(max_length=400,blank=False)
    desp = models.TextField(blank=False)
    pubdate = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.title)
    
class Video(models.Model):
    title_of_video = models.CharField(max_length=500)
    video_desp = models.TextField(blank=True)
    videofile = models.FileField(upload_to='videos/', null=True)
    pubdate = models.DateField(auto_now_add=True)
    playlist = models.OneToOneField(Playlist, on_delete=models.CASCADE, null=True)
 
    def __str__(self):
        return '%s' %(self.title_of_video)
    