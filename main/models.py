from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify
from os.path import splitext


class PizzaSize(models.Model):
    small = 'Small'
    medium = 'medium'
    large = 'large'
    size_choices = [
        (small, 'small'),
        (medium, 'medium'),
        (large, 'large')
    ]
    size = models.CharField(max_length=10, choices=size_choices, default=small)

    def get_price(self):
        if self.size == self.small:
            return 0
        elif self.size == self.medium:
            return 1.00
        elif self.size == self.large:
            return 2.00
        return 0.00

    def __str__(self):
        return self.size


def slugify_upload(instance, filename):
    folder = instance._meta.model_name
    name, ext = splitext(filename)
    name_t = slugify(name) or name
    return f'{folder}/{name_t}{ext}'


class Category(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    discount = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=slugify_upload, blank=True, null=True)
    condition = models.BooleanField(default=False, blank=True, null=True)

    def discount_calculation(self):
        if self.discount is not None:
            discount_amount = (self.price / 100) * self.discount
            discounted_price = self.price - discount_amount
            return discounted_price, self.price
        return None


class Order(models.Model):
    user_id = models.ForeignKey('auth.User', )




