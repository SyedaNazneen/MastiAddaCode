from django.db import models

# Create your models here.
# coding_zone_app/models.py

from django.db import models

class Video(models.Model):  # <--- Yahan 'V' capital hona chahiye
    title = models.CharField(max_length=200) 
    description = models.TextField() 
    video_url = models.URLField(unique=True) 
    upload_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.title