# relationship_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    CustomUser,
    UserProfile,
    Author,
    Library,
    Book,
    Librarian
)

# ---------------------------
# Custom User Admin
# ---------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        'username',
        'email',
        'date_of_birth',
        'is_staff',
        'is_superuser'
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

# Register remaining models
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Librarian)
