
from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
from comment.models import Comment

# Create your models here.

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


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
    STATUS_CHOICES = (
		('d', 'پیش‌نویس'),		 # draft
		('p', "منتشر شده"),		 # publish
		('i', "در حال بررسی"),	 # investigation
		('b', "برگشت داده شده"), # back
	)
    title = models.CharField(max_length=250 , verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400 , db_index=True ,allow_unicode=True , verbose_name='ادرس مقاله')
    category = models.ManyToManyField(Category , verbose_name="دسته بندی مقاله", related_name="articles_cat")
    description = models.TextField(verbose_name='توضیح مقاله')
    image = models.ImageField(upload_to='articles')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    is_special = models.BooleanField(default=False , verbose_name="مقالات ویژه")
    date = models.DateTimeField(auto_now_add=True , editable=False , verbose_name='تاریخ ایجاد مقاله')
    auther = models.ForeignKey(User , on_delete=models.CASCADE ,null=True, related_name="articles_cat" , verbose_name='نویسنده')
    comments = GenericRelation(Comment)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    class Meta:
        verbose_name = ' مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ['-date']


        def __str__(self):
            return self.title
        
    def get_absolute_url(self):
        return reverse('account:home')
    
    
    def image_tag(self):
        return format_html(( "<img src='{}' width=100 height=75 style='border-radius: 5px;'>".format(self.image.url)))
    image_tag.short_description='عکس'
    
    def category_to_str(self):
        return ". ".join([category.title for category in self.category.active() ])
    category_to_str.short_description = 'دسته بندی'

    objects = ArticleManager()