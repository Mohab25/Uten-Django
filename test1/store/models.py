from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    feature = models.CharField(max_length=200)
    product_type = models.CharField(max_length=150,default='')
    image = models.ImageField()
    vendor = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name 

    class Meta:
        ordering=['id']
