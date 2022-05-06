from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes',)


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)
    list_select_related = ('post', 'author',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
