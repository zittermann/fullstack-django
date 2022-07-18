from rest_framework import serializers
from thread.models.thread import Thread
from board.serializers.board import BoardSerializer


class ThreadSerializer(serializers.ModelSerializer):
    board = BoardSerializer

    class Meta:
        model = Thread
        fields = "__all__"
