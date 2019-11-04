from django.db import models

# Create your models here.

class Songs(models):
  # song title
  title = models.CharField(max_length=255, null=False)
  # artist name
  artist = models.CharField(max_length=255, null=False)

  def __str__(self):
    return "{} - {}".format(self.title, self.artist)