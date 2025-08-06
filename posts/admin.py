from django.contrib import admin

from posts.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_on', 'last_updated', )
    list_editable = ('published', )

# Enregistrement de notre model dans l'admin
admin.site.register(BlogPost, BlogPostAdmin)
