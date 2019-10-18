from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    account_balance = models.IntegerField()

    def __str__(self):
        return self.email

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=150)
    cost = models.IntegerField()
    no_of_products = models.IntegerField()

    def __str__(self):
        return self.product_name

class BuyProduct(models.Model):
    email = models.EmailField()
    product_name = models.CharField(max_length=50)
    cost = models.IntegerField(default = '0')
    items = models.IntegerField(default = '0')

    def __str__(self):
        return "{}--{}".format(self.email, self.product_name)