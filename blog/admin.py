from .models import Post, Category, Tag, About
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(About)
