from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', default=0, on_delete=models.CASCADE)
    shop = models.ManyToManyField('Shop', help_text='Выбор магазина')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
