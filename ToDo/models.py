from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 500)
    status = models.CharField(default = "Pending")

    def get_absolute_url(self):
        return reverse("todo:home")
    
    def get_landing_url(self):
        return reverse("todo:home")
    