from django.contrib import admin



from django.contrib import admin
from .models import Video  # <-- LINE 1: Hamne apne Video Model ko import kiya

# Register your models here.

admin.site.register(Video)  # <-- LINE 2: Hamne is Video Model ko Admin Panel mein dikhane ke liye register kiya