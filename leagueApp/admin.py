from django.contrib import admin
from models import (
    Hero,
    User)

# Pimps out the admin page


class HeroAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'primary_role',
        'secondary_role',
        'passive',
        'spell1',
        'spell2',
        'spell3',
        'spell4',)
    search_fields = ('title',)


class UserAdmin(admin.ModelAdmin):
    search_fields = ('user_name',)


admin.site.register(Hero, HeroAdmin)
admin.site.register(User, UserAdmin)
