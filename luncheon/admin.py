from django.contrib import admin

# Register your models here.
from .models import Eatery

class EateryAdmin(admin.ModelAdmin):
	list_display=('name', 'address', 'id')
	fields=['name', 'address', ('website_link', 'menu_link'), 'favorited_by']

admin.site.register(Eatery, EateryAdmin)
