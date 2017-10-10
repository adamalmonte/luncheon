from django.contrib import admin

# Register your models here.
from .models import Eatery


class EateryAdmin(admin.ModelAdmin):
	list_display=('name', 'address', 'inHouseStarRating', 'id')
	fields=['name', 'address', ('inHouseStarRating')]

admin.site.register(Eatery, EateryAdmin)
