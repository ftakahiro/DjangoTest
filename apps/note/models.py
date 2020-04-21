from django.db import models

# Create your models here.
class Note(models.Model):
    note_id=models.CharField(max_length=32)
    title=models.CharField(max_length=256)
    content=models.CharField(max_length=256)

    def __str__(self):
        return self.title
