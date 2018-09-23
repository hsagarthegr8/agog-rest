from django.contrib import admin

from .models import Post, Response, Reactions

admin.site.register(Post)
admin.site.register(Response)
admin.site.register(Reactions)
