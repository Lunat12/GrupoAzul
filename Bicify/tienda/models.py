from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse



class Registers(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    billing_address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    premium_user = models.BooleanField(default=False)
    admin_user = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id_user']


#@receiver(pre_save, sender=User)
#def roles(sender, instance, **kwargs):
    #if instance.premium_user and instance.admin_user:
        #raise ValidationError("No puedes ser tanto un usuario premium como un administrador al mismo tiempo.")

class Product(models.Model):

    CATEGORY_CHOICES =(
        ('Bicicletas','Bicicleta'),
        ('Accesorios','Accesorios'),
    )

    SUBCATEGORY_CHOICES =(
        ('Montaña','Montaña'),
        ('BMX','BMX'),
        ('Urbano','Urbano'),
        ('Grava','Grava'),
        ('Electrica','Electrica'),
        ('Accesorios','Accesorios'),
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
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)

    product_list = models.ManyToManyField(Product)

    def __str__(self):
        return f"Cart for {self.user.name}"

class Sale(models.Model):
    date_of_sale = models.DateField()
    product_list = models.ManyToManyField(Product)
    id_user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Sale on {self.date_of_sale}"


class Categories(models.Model):

    product_categories = models.CharField(max_length=255)

    # def get_absolute_url_categories(self):
    #     return reverse('',args=[str(self.product_categories)])


class Subcategories(models.Model):
    product_subcategories = models.CharField(max_length=255)

    def get_absolute_url_subcategories(self):
        return reverse('index',args=[str(self.product_subcategories)])


# Create your models here.
