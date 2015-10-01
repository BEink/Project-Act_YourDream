from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__','author','title','published_date']
    class Meta:
        mode = Post

admin.site.register(Post,PostAdmin)
