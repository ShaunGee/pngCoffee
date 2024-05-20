from django.db import models

# Create your models here.

'''
Creating a table for each coffee product. Each product will have:
-Name
-short description
-long description
-image
'''

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_short_description = models.TextField(max_length=30)
    product_long_description = models.TextField()
    product_img = models.ImageField(upload_to='')
    
    def __str__(self):
        return self.product_name
