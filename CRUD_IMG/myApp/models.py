from django.db import models

# Create your models here.
class CustomUser(models.Model):
    roll_no = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile= models.CharField(max_length=30)
    image  = models.ImageField(upload_to='',null=True, blank=True)
    
    def __str__(self):
        return self.roll_no