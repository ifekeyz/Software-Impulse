from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    identity = models.CharField(max_length=100,default=0, null=True,blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'



# Create your models here.
class Stock(models.Model):
    officer = models.CharField(max_length=100,blank=True)
    product_code = models.CharField(max_length=100,blank=True)
    color_type = models.CharField(max_length=100,blank=True,null=True)
    qty_receieved = models.IntegerField(blank=True,null=True)
    litre = models.CharField(max_length=100,blank=True)
    client_name = models.CharField(max_length=100,blank=True)
    is_admin = models.BooleanField(default=False)
    invoice_code = models.CharField(max_length=100,blank=True,null=True)
    stoke_keeper = models.CharField(max_length=100,blank=True,null=True)
    qty_issued = models.IntegerField(blank=True,null=True)
    qty_balance = models.IntegerField(blank=True,null=True)
    OPTION = (("Pending","Pending"),("Approved","Approved"))
    status = models.CharField(choices=OPTION, max_length=10, default="Pending")
    created = models.DateField(default = datetime.now, blank=True,null=True)
    OPTION = (("Collected","Collected"),("Not Collected","Not Collected"))
    pickStatus = models.CharField(max_length=50,choices=OPTION,default="Not Collected")



    def __str__(self):
        return self.product_code


class Bin(models.Model):
    product_code = models.CharField(max_length=100,blank=True)
    product_color = models.CharField(max_length=100,blank=True)
    initalQty = models.IntegerField(null=True,blank=True)
    qty = models.IntegerField()
    litre = models.CharField(max_length=100,blank=True)
    client_name = models.CharField(max_length=100,blank=True,null=True)
    OPTION = (("Pending","Pending"),("Approved","Approved"))
    status = models.CharField(choices=OPTION, max_length=10, default="Pending")
    updateQuantity = models.IntegerField(null=True,blank=True)
    list_date = models.DateField(auto_now=datetime, blank=True,null=True)


    def __str__(self) -> str:
        return f'{self.product_code}'