from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ELEC', 'Electronics'),
        ('CLOTH', 'Clothing'),
        ('FOOD', 'Food'),
        ('BOOK', 'Books'),
        ('OTHR', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='OTHR')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
