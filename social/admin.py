from django.contrib import admin
from .models import Post, Comment, UserProfile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'birth_date', 'location')
