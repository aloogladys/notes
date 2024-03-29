
from django.contrib import admin
from django.urls import path,include 
from notes_app.views import sign_in, register , success
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', sign_in),
    path('register/', register),
    path('success/', success),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
