from django.db import models

class Product(models.Model):
    '''Product '''
    title = models.CharField(max_length=200, verbose_name='Product Title')
    description = models.TextField(null=True, blank=True, verbose_name='Product Description')
    price = models.IntegerField(verbose_name='Product Price')

    preview_image = models.ImageField(null=True, blank=True, verbose_name='Product Preview Image')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-id']


class News(models.Model):
    '''News '''
    title = models.CharField(max_length=200, verbose_name='News Title')
    description = models.TextField(null=True, blank=True, verbose_name='News Description')
    image = models.ImageField(null=True, blank=True, verbose_name='News Image')    
    

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-id']

