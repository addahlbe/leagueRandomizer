from django.contrib import admin
from models import (
    Hero)

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


admin.site.register(Hero, HeroAdmin)
