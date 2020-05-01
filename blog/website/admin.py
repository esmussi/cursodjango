from django.contrib import admin
from .models import Post
from .models import Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name']
    search_fields = ['title', 'sub_title']

admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['nome', 'phone']
    search_fields = ['nome', 'phone']

admin.site.register(Contact, ContactAdmin)