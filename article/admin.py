from django.contrib import admin
from .models import Article , Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title', 'slug', 'status' , 'parent')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category , CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug' ,'status' , 'category_to_str')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status']

    def category_to_str(self , obj):
        return ". ".join([category.title for category in obj.category_published()])
    category_to_str.short_description = 'دسته بندی'

admin.site.register(Article , ArticleAdmin)