from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class admin(admin.ModelAdmin):
	list_display = ('title','author','created_at')
	search_fields = ('title','summary')
	prepopulated_fields = {'slug':('title',)}