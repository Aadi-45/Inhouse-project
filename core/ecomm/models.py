from django.db import models

# Create your models here.

SIZE = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
)

CATEGORIES = (
    ('SH','Shirt'),
    ('TS','T-Shirt'),
    ('TR','Trouser'),
)

class Product(models.Model):
    title = models.CharField(max_length=120)
    desc = models.CharField(max_length=500)
    price = models.FloatField(default=0.00)
    size = models.CharField(choices=SIZE, max_length=2)
    category = models.CharField(choices=CATEGORIES, max_length=2)
    img1 = models.ImageField(upload_to='ecomm/images', default='')
    img2 = models.ImageField(upload_to='ecomm/images', default='')
    img3 = models.ImageField(upload_to='ecomm/images', default='')

    def __str__(self):
        return self.title

