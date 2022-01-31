from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


class Category(models.Model):
    image = models.ImageField(
        upload_to='media/category', blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        db_table = ''
        managed = True
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return self.image.url
        return ''


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=400, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='media/products', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media/products', blank=True, null=True)
    available = models.BooleanField(default=True)
    shipping_day = models.IntegerField(default=3)
    quantity = models.IntegerField(default=1)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        db_table = ''
        managed = True
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http:127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http:127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_to = BytesIO()
        img.save(thumb_to, 'JPEG', quality=85)
        thumbnail = File(thumb_to, name=image.name)
        return thumbnail
