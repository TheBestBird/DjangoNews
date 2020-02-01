from django.contrib import admin
from .models import News
# Register your models here.

# admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'time_publish', 'status']
    list_filter = ['status', 'time_create', 'time_publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'time_publish'
    ordering = ('-status', '-time_publish')
