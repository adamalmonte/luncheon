from django.contrib import admin

# Register your models here.
from .models import Eatery


class EateryAdmin(admin.ModelAdmin):
	list_display=('name', 'open_now', 'address', 'walking_distance', 'inHouseStarRating', 'googleStarRating', 'priceLevel')
	# list_filter=('name', 'inHouseStarRating')
	fields=['name', 'address', ('inHouseStarRating', 'googleStarRating'), ('priceLevel', 'hoursOfOperation'), 'link']

admin.site.register(Eatery, EateryAdmin)
