from django.db import models

from board.models.board import Board

class Thread(models.Model):
    code = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=8000)

    board = models.ForeignKey(
        Board,
        related_name="board_threads",
        on_delete=models.CASCADE,
        null=False,
    )

    def __str__(self) -> str:
        return f'{self.subject}: ({self.code})'

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"
