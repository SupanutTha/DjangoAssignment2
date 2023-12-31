from django.db import models

# Create your models here.
#ENUM
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)

class LoginAttempt(models.Model):
    UID = models.UUIDField
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Assuming you store hashed passwords
    result = models.CharField(max_length=20)  # 'Success' or 'Failure'
    timestamp = models.DateTimeField(auto_now_add=True)
    def as_dict(self):
        return {
            'result': self.result,
            'email': self.email,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        }
    def __str__(self):
        return self.email
    
class Product(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    product_id = models.CharField(max_length=20)
    product_title = models.CharField(max_length=200)
    product_unit = models.CharField(max_length=50)
    display_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    description = models.CharField(max_length=250)

    product_pic = models.CharField(max_length=200, blank=True)

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.product_id



class Traveler(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    password = models.CharField(max_length=250)

    # Database fields
    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.username

