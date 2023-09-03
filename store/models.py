from django.db import models
import datetime
import os
# Create your models here.

def get_file_path(request,filename):
    original_filename =filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True)
    description=models.TextField(max_length=150,null=False,blank=False)  
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    product_image=models.ImageField(upload_to=get_file_path,null=True)

    def __str__(self):
        return self.product_name



