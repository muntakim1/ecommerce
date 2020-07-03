from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

# category model
class Category(models.Model):
    Category_Name = models.CharField(max_length=240)
    slug = models.SlugField()

    def __str__(self):
        return self.slug





# Product
class Product(models.Model):
    Product_name = models.CharField(max_length=250)
    Product_Code = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Product_slug = models.SlugField()
    Product_Description = models.TextField()
    UnitPrice = models.DecimalField(max_digits=5, decimal_places=2)
    StockOut = models.BooleanField(default=False)
    images = models.ImageField(upload_to='product/%Y/%m/%d/')
    available = models.BooleanField(default=False)
    discount = models.IntegerField()
    new_Arraivel = models.BooleanField(default=False)
    stars = models.IntegerField(default=4)
    Trending = models.BooleanField(default=False)
    Product_Update = models.DateField(default=timezone.now)

    class Meta:
        index_together = (('id', 'Product_slug'),)

    def __str__(self):
        return self.Product_Code

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.Product_slug, ])


#Order Tracking 

class OderTracking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    InvoiceId=models.CharField(max_length=250)
    Date=models.CharField(max_length=250,default="")
    ProductCode = models.OneToOneField(Product,on_delete=models.CASCADE)
    Pending = models.BooleanField(default=True)
    Confirmed = models.BooleanField(default=False)
    Proceesing = models.BooleanField(default=False)
    Packed = models.BooleanField(default=False)
    Shipped = models.BooleanField(default=False)
    Delivered = models.BooleanField(default=False)
    def __str__(self):
        return self.InvoiceId

# Cart
class Cart(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE,default="")
    Cart_Price = models.DecimalField(max_digits=4, decimal_places=2)
    Cart_Quantity = models.IntegerField()
    size = models.CharField(max_length=240, default="small")
    Cart_total = models.DecimalField(max_digits=4, decimal_places=2)
    Delivery_Charge = models.DecimalField(max_digits=4, decimal_places=2)
    Discount = models.DecimalField(max_digits=4, decimal_places=2)
    Total = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.Product_Code


# Transactions



class Transactions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    state_country = models.CharField(max_length=255)
    street_Address = models.CharField(max_length=255)
    appertment = models.CharField(max_length=255,null=True)
    town = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    phone=models.CharField(max_length=11)
    email= models.EmailField()
    payment_Method = models.CharField(max_length=255)
    Total = models.CharField(max_length=255)
    