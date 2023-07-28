from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300,default="nothing is to describe")
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    cart=models.BooleanField(default=False)
    qty=models.IntegerField(default=0)
    total=models.IntegerField(default=1)


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000,default='none')
    qty=models.IntegerField(default=0)
    name = models.CharField(max_length=111)
    phone = models.CharField(max_length=70, default="")
    email = models.CharField(max_length=70, default="")
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    address = models.CharField(max_length=11)
    pub_date = models.DateTimeField(default=timezone.now)
    # created_at = models.DateTimeField(False, True, editable=False)

    def __str__(self):
        return self.name