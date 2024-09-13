from rest_framework import viewsets
from .models import AudioFile
from .serializers import AudioFileSerializer

class AudioFileViewSet(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SendTextView(APIView):
    def post(self, request, format=None):
        text = request.data.get('text')
        if text:
            return Response({'message': 'ajdjdjaldkfjadlfjkasdpoifjasop`l;kfjadspkl;fhjasd`f'}, status=status.HTTP_200_OK)
        return Response({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)


