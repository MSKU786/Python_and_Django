from django.contrib import admin
from blog.models import Post,Comments


admin.site.register(Comments)
admin.site.register(Post)
# Register your models here.
