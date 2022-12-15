from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image_url = models.URLField(blank=True)
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk': self.pk})