from statistics import mode
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


class Information(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    Twitter = models.URLField(max_length=200, null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    description = models.TextField()

    class Meta:
        managed = True
        verbose_name = 'Information'
        verbose_name_plural = 'Information'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
