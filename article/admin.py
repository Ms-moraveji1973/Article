from django.contrib import admin
from .models import Article , Category

# Register your models here.
def make_published(modeladmin , request , queryset):
    queryset.update(status=True)
make_published.short_description = "انتشار مقاله ی انتخاب شده"

def make_draft(modeladmin , request , queryset):
    queryset.update(status=False)
make_draft.short_description = "پیش نویس مقاله ی انتخاب شده"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title', 'slug', 'status' , 'parent')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category , CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('image_tag' ,'title' ,'auther','slug' ,'status' , 'category_to_str')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status']
    actions = [make_published , make_draft]


    def category_to_str(self , obj):
        return ". ".join([category.title for category in obj.category.active() ])
    category_to_str.short_description = 'دسته بندی'

admin.site.register(Article , ArticleAdmin)