from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
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
    
@receiver(pre_save, sender=User)
def roles(sender, instance, **kwargs):
    if instance.premium_user and instance.admin_user:
        raise ValidationError("No puedes ser tanto un usuario premium como un administrador al mismo tiempo.")

class Product(models.Model):

    CATEGORY_CHOICES =(
        ('Bicicletas','Bicicleta'),
        ('Bicileta de Montaña','Bicileta de Montaña'),
        ('Bicicleta Hibrida','Bicicleta Hibrida'),
        ('Bicicleta BMX','Bicicleta BMX'),
    )

    SUBCATEGORY_CHOICES =(
        ('Sillines','Sillines'),
        ('Cadenas','Cadenas'),
        ('Ruedas','Ruedas'),
        ('Bomba de aire','Bomba de aire'),
        ('Manguitos','Manguitos'),   
        ('Candado','Candado'),
        )

    product_name = models.CharField(max_length=255)
    product_images = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,blank=True, null=True)
    subcategory = models.CharField(max_length=100, choices=SUBCATEGORY_CHOICES, blank=True, null=True)
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

# Create your models here.
