from rest_framework import viewsets
from thread.serializers.thread import (
    Thread,
    ThreadSerializer
)

# Create your views here.
class ThreadViewset(viewsets.ModelViewSet):

    serializer_class = ThreadSerializer
    queryset = Thread.objects.all().order_by("-code")