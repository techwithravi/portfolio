from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CAT = ((1, 'Beagle'), (2, 'Bulldog'), (3, 'German Shepherd'), (4, 'Poddle'), (5, 'English Springer Spaniel'),
           (6, 'Airedale Terrier'))
    name = models.CharField(max_length=50, verbose_name='Product Name')
    price = models.FloatField()
    age = models.IntegerField()
    cat = models.IntegerField(max_length=50, verbose_name='Category', choices=CAT)
    pdetail = models.CharField(max_length=300, verbose_name='Product Details')
    is_active = models.BooleanField(default=True)
    pimage = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name


class contactenquiry(models.ModelAdmin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()


class Order(models.Models):
    orderid = models.IntegerField()
    uid = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='uid')
    pid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='pid')
    qty = models.IntegerField(default=1)
    amt = models.FloatField()


class Orderhistory(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


class Cart(models.Models):
    uid = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='uid')
    pid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='pid')
    qty = models.IntegerField(default=1)

