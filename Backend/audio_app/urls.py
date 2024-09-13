from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from audio_app.views import AudioFileViewSet
from audio_app.views import AudioFileViewSet, SendTextView  # Import SendTextView


# Set up the router for API routes
router = DefaultRouter()
router.register(r'audio', AudioFileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin route
    path('api/', include(router.urls)),       # API routes for audio files
    path('api/send-text/', SendTextView.as_view(), name='send-text'),  # Add your custom route here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
