# MastiAddaProject/urls.py

from django.contrib import admin
from django.urls import path, include
# Naya import: redirect function
from django.views.generic.base import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', include('coding_zone_app.urls')),
    
    # Yeh line ab base URL (/) ko /videos/ par bhej degi
    path('', RedirectView.as_view(url='videos/', permanent=True), name='index'),
]