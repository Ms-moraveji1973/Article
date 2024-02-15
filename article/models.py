from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.html import format_html

# Create your models here.

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status=True)


class CatagoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

class Category(models.Model):
    parent = models.ForeignKey('self',default=False , null=True , blank=True , on_delete=models.SET_NULL , related_name="children" , verbose_name="زیر دسته" )
    title = models.CharField(max_length=250 , verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=400 , db_index=True ,allow_unicode=True , verbose_name='ادرس دسته بندی')
    status = models.BooleanField(default=True , verbose_name='قعال / غیر فعال')
    position = models.IntegerField()

    class Meta:
        verbose_name = ' دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقاله ها'
        ordering = ['parent__id' , 'position']
        
    def __str__(self):
        return self.title
    
    objects = CatagoryManager()

class Article(models.Model):
    title = models.CharField(max_length=250 , verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400 , db_index=True ,allow_unicode=True , verbose_name='ادرس مقاله')
    category = models.ManyToManyField(Category , verbose_name="دسته بندی مقاله", related_name="articles_cat")
    description = models.TextField(verbose_name='توضیح مقاله')
    image = models.ImageField(upload_to='articles')
    status = models.BooleanField(default=True , verbose_name='قعال / غیر فعال')
    date = models.DateTimeField(auto_now_add=True , editable=False , verbose_name='تاریخ ایجاد مقاله')
    auther = models.ForeignKey(User , on_delete=models.CASCADE ,null=True, related_name="articles_cat" , verbose_name='نویسنده')


    class Meta:
        verbose_name = ' مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ['-date']


        def __str__(self):
            return self.title
        
    def get_absolute_url(self):
        return reverse('home')
    
    
    def image_tag(self):
        return format_html(( "<img src='{}' width=100 height=75 style='border-radius: 5px;'>".format(self.image.url)))
    image_tag.short_description='عکس'
    
    def category_to_str(self):
        return ". ".join([category.title for category in self.category.active() ])
    category_to_str.short_description = 'دسته بندی'

    objects = ArticleManager()