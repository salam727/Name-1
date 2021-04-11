from django.contrib import admin
from .models import Article ,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status')
    list_filter = (['status'])
    search_fields = ('title','slug')


admin.site.register(Category,CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','jpublish','status','category_to_str')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    ordering = ['-status', '-publish']

    def category_to_str(self, obj):
        return "Categories"
admin.site.register(Article,ArticleAdmin)
