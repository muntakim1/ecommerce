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


# Cart
class Cart(models.Model):
    Product_Code = models.CharField(max_length=20)
    Cart_Price = models.DecimalField(max_digits=4, decimal_places=2)
    Cart_Quantity = models.IntegerField()
    size = models.CharField(max_length=240, default="small")
    Cart_total = models.DecimalField(max_digits=4, decimal_places=2)
    Delivery_Charge = models.DecimalField(max_digits=4, decimal_places=2)
    Discount = models.DecimalField(max_digits=4, decimal_places=2)
    Total = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.Product_Code


# Check_out

class CheckOut(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Country = models.CharField(max_length=240)
    Street_Address = models.CharField(max_length=250)
    City = models.CharField(max_length=20)
    ZIP_Code = models.CharField(max_length=10)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Payment_Method = models.CharField(max_length=240)
    Delivery_Charge = models.DecimalField(max_digits=4, decimal_places=2)
    Discount = models.DecimalField(max_digits=4, decimal_places=2)
    Total = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.user.username
