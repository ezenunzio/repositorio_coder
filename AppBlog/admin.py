from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

'''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'author', 'imagen')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')
'''