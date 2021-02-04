from django.contrib import admin
from django.contrib import admin
from .models import Ads
from .models import Category


class AdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'category')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Ads,AdsAdmin)
admin.site.register(Category)