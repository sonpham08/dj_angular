from django.db import models
from django.contrib.auth import get_user_model
# from user.models import User
User = get_user_model()

# Create your models here.
class Coin(models.Model):
    coin_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)

class Transporter(models.Model):
    transporter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    size = models.CharField(max_length=255)
    hdh = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    CPU = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)
    pay_type = models.IntegerField(default=0) # 0: tien mat, 1: 1 Card
    gurantee = models.CharField(max_length=255)
    promotion = models.IntegerField()
    start_promo = models.DateTimeField()
    end_promo = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s..." % self.myfield

class FlashSale(models.Model):
    flash_id = models.AutoField(primary_key=True)
    start_flash = models.DateTimeField()
    end_flash = models.DateTimeField()

class FlashProduct(models.Model):
    flashproduct = models.AutoField(primary_key=True)
    flashsale = models.ForeignKey(FlashSale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    num_buy = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

class StatusProduct(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    price = models.IntegerField(default=0)
    transporter = models.ForeignKey(Transporter, on_delete=models.DO_NOTHING, default=1) # GHN

    def __str__(self):
        return self.name


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    total_price = models.IntegerField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=255) 
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    status_product = models.ForeignKey(StatusProduct, on_delete=models.CASCADE, default=1)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class DealedProduct(models.Model):
    dealed_id = models.AutoField(primary_key=True)
    number_product_dealed = models.IntegerField() # so luong san pham da ban cho 1 san pham
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

class DetailOrder(models.Model):
    detail_id = models.AutoField(primary_key=True)
    number_product_order = models.IntegerField() 
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING, default=0)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    time_comment = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)