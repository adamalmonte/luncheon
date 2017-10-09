from django.contrib import admin

# Register your models here.
from .models import Eatery


class EateryAdmin(admin.ModelAdmin):
	list_display=('name', 'open_now', 'address', 'walking_distance', 'inHouseStarRating', 'get_google_rating', 'get_google_price_level', 'id')
	fields=['name', 'address', ('inHouseStarRating'), 'link']

admin.site.register(Eatery, EateryAdmin)
