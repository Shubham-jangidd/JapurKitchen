from django.db import models




# Create your models here.
class contactus(models.Model):
    """Description: Customer Address."""
    first_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 150)
    message = models.CharField( max_length = 2000)
    def __str__(self):
        return self.email


