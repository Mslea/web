from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','datetime']
    list_filter = ['datetime']
    search_fields = ['title','id']
admin.site.register(Post,PostAdmin)