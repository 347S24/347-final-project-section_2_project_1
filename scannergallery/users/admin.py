from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from .models import Tags,Image,Album

from scannergallery.users.forms import (
    UserChangeForm,
    UserCreationForm,
)

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        ("User", {"fields": ("name",)}),
    ) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]



class TagsInline(admin.TabularInline):
    model=Tags

class TagsAdmin(admin.ModelAdmin):
    list_display=["name"]
    
class ImageAdmin(admin.ModelAdmin):
    list_display=("name", "time_date")
    

class AlbumAdmin(admin.ModelAdmin):
    list_display=("name", "display_pattern")
    

admin.site.register(Tags, TagsAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)

