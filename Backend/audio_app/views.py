from rest_framework import viewsets
from .models import AudioFile
from .serializers import AudioFileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# audio_app/views.py

import os
from django.conf import settings
from django.http import JsonResponse
from django.views import View

import os
import base64
from django.conf import settings
from django.http import JsonResponse, Http404
from django.views import View

class ListMediaFilesView(View):
    def get(self, request, *args, **kwargs):
        media_root = settings.MEDIA_ROOT
        media_url = settings.MEDIA_URL
        
        # List to hold file information
        files = []

        # Walk through the media directory
        for root, dirs, filenames in os.walk(media_root):
            for filename in filenames:
                # Construct the full file path
                file_path = os.path.join(root, filename)
                
                # Read and encode the file
                try:
                    with open(file_path, 'rb') as file:
                        encoded_file = base64.b64encode(file.read()).decode('utf-8')
                except Exception as e:
                    continue  # Skip files that can't be read

                # Construct the URL for the file
                relative_path = os.path.relpath(file_path, media_root)
                file_url = os.path.join(media_url, relative_path).replace("\\", "/")

                files.append({
                    'url': file_url,
                    'data': encoded_file,
                    'name': filename
                })

        return JsonResponse({'files': files})



class AudioFileViewSet(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer


class SendTextView(APIView):
    def post(self, request, format=None):
        text = request.data.get('text')
        if text:
            return Response({'message': 'ajdjdjaldkfjadlfjkasdpoifjasop`l;kfjadspkl;fhjasd`f'}, status=status.HTTP_200_OK)
        return Response({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)