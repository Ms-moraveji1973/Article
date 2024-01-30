from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250 , verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=400 , db_index=True ,allow_unicode=True , verbose_name='ادرس دسته بندی')
    status = models.BooleanField(default=True , verbose_name='قعال / غیر فعال')
    position = models.IntegerField()

    class Meta:
        verbose_name = ' دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقاله ها'
        ordering = ['position']
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=250 , verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400 , db_index=True ,allow_unicode=True , verbose_name='ادرس مقاله')
    category = models.ManyToManyField(Category , verbose_name="دسته بندی مقاله")
    description = models.TextField(verbose_name='توضیح مقاله')
    image = models.ImageField(upload_to='articles')
    status = models.BooleanField(default=True , verbose_name='قعال / غیر فعال')
    date = models.DateTimeField(auto_now_add=True , editable=False , verbose_name='تاریخ ایجاد مقاله')
    auther = models.ForeignKey(User , on_delete=models.CASCADE ,null=True, verbose_name='نویسنده')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ' مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ['-date']