from django.db import models

class UserProfile(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  bio = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.name)
