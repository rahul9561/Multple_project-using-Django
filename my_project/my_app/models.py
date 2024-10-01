from django.db import models

from datetime import datetime


class Catogory(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    # product_id=models.AutoField(primary_key=True)
    category = models.ForeignKey(Catogory, on_delete=models.CASCADE,default="2")
    product_name = models.CharField(max_length=250,null=True)
    product_price = models.CharField(max_length=250,null=True)
    created_at = models.DateTimeField(("Created At"), auto_now_add=True, null=True)
    image = models.ImageField(upload_to='products/')
    desc = models.TextField()

    def __str__(self):
        return self.product_name



    # @staticmethod
    # def get_all_product_by_category(category_id=None):
    #     if category_id:
    #         return Product.objects.filter(category=category_id)
    #     else:
    #         return Product.objects.all()



class Signup(models.Model):
    username=models.CharField(max_length=150)
    email=models.EmailField()   
    password=models.CharField(max_length=200) 

    def __str__(self):
        return self.username
    





class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()
    field3 = models.IntegerField()



class Crud(models.Model):
    task=models.CharField(max_length=123)
    is_completes=models.BooleanField(default=False)
    create_at=models.DateField(auto_now_add=True)
    updates_at=models.DateField(auto_now=True)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name


class demo(models.Model):
    name=models.CharField(max_length=120,null=True)
    price=models.CharField(max_length=120)


    def __str__(self):
        return self.name
    



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title



class Books(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=128)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )

    def __str__(self):
        return self.title
    

class Youtube_thum(models.Model):
    url_name=models.CharField(max_length=120)


    def __str__(self):
        return self.url_name