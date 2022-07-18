from rest_framework import viewsets
from thread.serializers.thread import (
    Thread,
    ThreadSerializer
)

# Create your views here.
class ThreadViewset(viewsets.ModelViewSet):
    queryset = Thread.objects.all().order_by("code")
    serializer_class = ThreadSerializer
