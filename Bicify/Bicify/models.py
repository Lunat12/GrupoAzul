
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    billing_address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    premium_user = models.BooleanField(default=False)
    admin_user = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_images = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    size = models.CharField(max_length=20, blank=True, null=True)
    battery_h = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_list = models.ManyToManyField(Product)

    def __str__(self):
        return f"Cart for {self.user.name}"

class Sale(models.Model):
    date_of_sale = models.DateField()
    product_list = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sale on {self.date_of_sale}"