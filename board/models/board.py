from django.db import models

class Board(models.Model):
    identifier = models.CharField(unique=True, max_length=4)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=280)

    def __str__(self) -> str:
        return f"{self.name}".capitalize()

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"
