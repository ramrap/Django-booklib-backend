
from django.contrib import admin
from .models import Book
# Register your models here.
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','description']
    search_fields=['title','description']
    list_filter=['published']
