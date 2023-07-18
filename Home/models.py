from django.db import models

# Create your models here.
class Items(models.Model):
    image = models.ImageField(upload_to='image/', default=None, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    Price = models.TextField()

class Secitems(models.Model):
    image = models.ImageField(upload_to='image/', default=None, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    Price = models.TextField()



class Wecitems(models.Model):
    image = models.ImageField(upload_to='image/', default=None, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    Price = models.TextField()


class cecitems(models.Model):
    image = models.ImageField(upload_to='image/', default=None, null=True)
    title = models.CharField(max_length=200)
    Price = models.TextField()
    disPrice = models.TextField()

class fecitems(models.Model):
    image = models.ImageField(upload_to='image/', default=None, null=True)
    title = models.CharField(max_length=200)
    Price = models.TextField()

