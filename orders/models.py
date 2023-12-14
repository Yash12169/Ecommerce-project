from django.db import models
from authentication.models import User
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
from products.models import Product

PAYMENT_MODE = Choices(
    (1,"cod",_("cod")),
    (2,"card",_("card")),
    (3,"UPI",_("UPI")),
    (4,"netbanking",_("netbanking")),
)

PAYMENT_STATUS = Choices(
    (1,"pending",_("pending")),
    (2,"completed",_("completed"))
)
# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_amount = models.IntegerField(default=0)
    payment_mode = models.IntegerField(choices=PAYMENT_MODE,default=PAYMENT_MODE.cod)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS,default=PAYMENT_STATUS.pending)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)



class OrderItems(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)