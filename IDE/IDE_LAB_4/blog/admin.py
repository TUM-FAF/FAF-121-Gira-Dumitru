from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']


admin.site.register(Blog, BlogAdmin)
