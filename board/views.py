from rest_framework import viewsets
from board.serializers.board import (
    Board,
    BoardSerializer
)

# Create your views here.
class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by("name")
    serializer_class = BoardSerializer
