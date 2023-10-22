from django.contrib import admin

# Register your models here.
from users.models import User


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('pk', 'email', )

