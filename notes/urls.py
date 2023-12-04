
from django.contrib import admin
from django.urls import path
from notes_app.views import sign_in
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_in),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
