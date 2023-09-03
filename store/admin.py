from django.contrib import admin
from store.models import BookShopeModel
# Register your models here.

# admin.site.register(BookStoreModel)

class BookShopeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category', 'first_pub', 'last_pub')

admin.site.register(BookShopeModel, BookShopeModelAdmin)