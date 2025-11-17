
# coding_zone_app/views.py

from django.shortcuts import render
from .models import Video  # Video Model ko import kiya

# Yeh function saare videos ko database se nikal kar template ko bhejega
def video_list(request):
    # Database se saare videos nikal liye
    all_videos = Video.objects.all().order_by('-upload_date') 
    
    # Template (HTML) ko data bhejte hain
    context = {'videos': all_videos}
    
    # 'video_list.html' template ko load karte hain
    return render(request, 'coding_zone_app/video_list.html', context)