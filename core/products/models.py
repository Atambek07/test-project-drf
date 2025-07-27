from django.db import models

class Product(models.Model):
    '''Product '''
    title = models.CharField(max_length=200, verbose_name='Product Title')
    description = models.TextField(null=True, blank=True, verbose_name='Product Description')
    price = models.IntegerField(verbose_name='Product Price')

    preview_image = models.ImageField(null=True, blank=True, verbose_name='Product Preview Image')

    bonus_count = models.IntegerField(verbose_name='Product Bonus Count', blank=True, null=True)
    old_price = models.IntegerField(verbose_name='Product Old Price', blank=True, null=True)
    full_description = models.TextField(verbose_name='Product Full Description', max_length=200)
    is_on_sale = models.BooleanField(verbose_name='Product On Sale', default=False)

    weight = models.FloatField(verbose_name='Product Weight', default=0.0)
    country_production = models.CharField(verbose_name='Products production country')
    brend = models.CharField(verbose_name='Product Brend', max_length=200, blank=True, null=True)


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

class Car(models.Model):
    '''Car '''

    currency = [
        ("Сом", "Сом"),
        ("Доллар", "$")
    ]

    name = models.CharField(max_length=200, verbose_name='Car Name')
    price = models.IntegerField(verbose_name='Car Price', blank=True, null=True)
    year = models.IntegerField(verbose_name='Car Year', blank=True, null=True)
    country_production = models.CharField(verbose_name='Car Country Production', max_length=200, blank=True, null=True)
    brend = models.CharField(verbose_name='Car Brend', max_length=200, blank=True, null=True)
    weight = models.FloatField(verbose_name='Car Weight', blank=True, null=True)
    color = models.CharField(verbose_name='Car Color', max_length=200, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, verbose_name='Car Photo')
    currency = models.CharField(verbose_name='Car Currency', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Car'