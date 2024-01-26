from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=250 , verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400 , db_index=True ,allow_unicode=True , verbose_name='ادرس مقاله')
    description = models.TextField(verbose_name='توضیح مقاله')
    image = models.ImageField(upload_to='articles')
    is_active = models.BooleanField(default=True , verbose_name='قعال / غیر فعال')
    date = models.DateTimeField(auto_now_add=True , editable=False , verbose_name='تاریخ ایجاد مقاله')
    auther = models.ForeignKey(User , on_delete=models.CASCADE ,null=True, verbose_name='نویسنده')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ' مقاله'
        verbose_name_plural = 'مقاله ها'
