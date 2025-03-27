from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    """Custom user model extending Django's AbstractUser"""
    #is_seller = models.BooleanField(default=False)  # Flag to differentiate buyers and sellers
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Avoids conflict with default User model
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Avoids conflict with default User model
        blank=True,
    )

    def __str__(self):
        return self.username



# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Cart"

# Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

# OrderItem Model (through model for Many-to-Many)
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} in Order #{self.order.id}"

"""# Payment Model
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="pending")
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"
"""