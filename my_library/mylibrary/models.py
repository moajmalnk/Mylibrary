from django.db import models
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'language'
        verbose_name_plural = 'languages'

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='pics', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('mylibrary:products_by_category', args=[self.slug])


class Book_details(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, max_length=250)
    auther = models.CharField(max_length=250)
    desc = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField(default=20)
    img = models.ImageField(upload_to='pics')
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'book_detail'
        verbose_name_plural = 'book_details'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('mylibrary:product_category_details ', args=[self.category.slug, self.slug])


class Patron(models.Model):
    name = models.CharField(max_length=250, unique=True)
    img = models.ImageField(upload_to='pics')
    phone = models.IntegerField()
    gmail = models.EmailField()
    card_no = models.IntegerField(default=10091)

    class Meta:
        ordering = ('name',)
        verbose_name = 'patron'
        verbose_name_plural = 'patrons'

    def __str__(self):
        return '{}'.format(self.name)
