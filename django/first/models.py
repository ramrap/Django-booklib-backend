from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=36,null=True,blank=False,unique=True,default='')
    description=models.TextField(max_length=256,blank=True)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=10)
    published=models.DateField(blank=True,default=None,null=True)
    cover=models.ImageField(upload_to='covers/',blank=True)

    def __str__(self):
        return self.title
    