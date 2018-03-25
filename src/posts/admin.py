from django.contrib import admin


# Register your models here.
from .models import Post    # .models INSTEAD OF post.models B/C ADMIN IS IN THE SAME FILE (RELATIVE IMPORT)


# ALLOWS CUSTOMIZATION TO ADMIN PAGE
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]      # WHAT YOU WANT TO DISPLAY
    list_display_links = ["updated"]                      # CHANGES WHAT YOU WANT TO LINK
    list_filter = ["updated", "timestamp"]                # ADDS FILTERING SYSTEM
    list_editable = ["title"]                             # LETS YOU EDIT TITLE
    search_fields = ["title", "content"]                  # ADDS SEARCH FILTER
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

