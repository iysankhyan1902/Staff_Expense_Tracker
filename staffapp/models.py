from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Expenses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=80)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.description} - ₹{self.amount} on {self.date}"