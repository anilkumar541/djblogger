from django.contrib import admin
from mainapp.models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["id", "title", "sub_title", "slug", "author", "content", "created_at", "updated_at", "status"]
    
