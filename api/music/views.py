from rest_framework import generics
from .models import Song
from .serializers import SongSerializer

class ListSongsView(generics.ListAPIView):
  """
  Gets all songs & returns them as a serialized JSON array.
  """
  queryset = Song.objects.all()
  serializer_class = SongSerializer
  