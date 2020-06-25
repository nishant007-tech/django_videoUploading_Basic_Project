from django.contrib import admin
from .models import Profile, Contact, Playlist, Video
# Register your models here.
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Playlist)
admin.site.register(Video)