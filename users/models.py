from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, EmailValidator, RegexValidator


# Create your models here.
class User(AbstractUser):
    name = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                limit_value=5, message="Name must be at least 5 characters long."
            )
        ],
    )
    email = models.CharField(
        max_length=200,
        unique=True,
        validators=[EmailValidator(message="Invalid email address.")],
    )
    password = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                limit_value=8, message="Password must be at least 8 characters long."
            ),
            RegexValidator(
                regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).*$",
                message="Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character.",
            ),
        ],
    )

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
