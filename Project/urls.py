from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Pages.urls')),
    path('Pages/',include('Pages.urls')),
    path('Pages/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
