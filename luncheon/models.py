from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
import urllib
import googlemaps
from .apikeys import get_gmaps_api_key

gmapsAPIkey = get_gmaps_api_key()
gmaps = googlemaps.Client(key=gmapsAPIkey)

#defining some variables we wlll need
fueledAddress="568 Broadway, New York, NY"
safeFueledAddress = urllib.parse.quote(fueledAddress, safe='')

"""
heavy inspiration from:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
and
https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
"""

# Create your models here.
class Eatery(models.Model):
	# Fields
	name = models.CharField(
		max_length=255,
		help_text="Enter the eatery's name!",
		verbose_name="Eatery Name",
	)
	
	address = models.CharField(
		max_length=255,
		blank=True,
		null=True
	)

	inHouseStarRating = models.IntegerField(
		verbose_name="Star Rating (Fueled)",
		validators = [
			MaxValueValidator(5),
			MinValueValidator(1)
		],
		blank=True,
		null=True
	)
	
	hoursOfOperation = models.DurationField(
		verbose_name="Hours of Operation",
		blank=True,
		null=True
	)
	
	link = models.URLField(
		blank=True,
		null=True
	)

	# Metadata
	class Meta:
		ordering = ["inHouseStarRating"]
		verbose_name_plural = "eateries"

	# Methods
	def get_absolute_url(self):
	    """
	    Returns the url to access a particular instance of the model.
	    """
	    return reverse('eatery-detail', args=[str(self.id)])

	def __str__(self):
		return self.name

	def walking_distance(self):
		if (self.address is None):
			return "Unknown :("

		distance_matrix = gmaps.distance_matrix(fueledAddress, self.address, mode="walking")
		return distance_matrix['rows'][0]['elements'][0]['duration']['text']

	def maps_link(self):
		safeAddress = urllib.parse.quote(self.address, safe='')

		if safeAddress:
			maps_link = 'https://www.google.com/maps/search/?api=1&query=' + safeAddress
			return maps_link

		return ''

	def directions_link(self):
		safeAddress = urllib.parse.quote(self.address, safe='')

		if safeAddress:
			directions_link = 'https://www.google.com/maps/dir/?api=1&origin=' + safeFueledAddress + '&destination=' + safeAddress
			return directions_link

		return ''

	def open_now(self):
		details = gmaps.places(self.name)

		try:
			if details['results'][0]['opening_hours']['open_now']:
				return "Yes!"
			else:
				return "Nope!"
		except KeyError:
			pass

		return "Unsure!"

	def get_google_rating(self):
		details = gmaps.places(self.name)

		try:
			if details['results'][0]['rating']:
				return details['results'][0]['rating']
		except KeyError:
			pass

		return ''

	def get_google_price_level(self):
		details = gmaps.places(self.name)
		priceString = ''

		try:
			if details['results'][0]['price_level']:
				for i in range(details['results'][0]['price_level']):
					priceString += '$'
		except KeyError:
			pass

		return priceString

	open_now.short_description="Open Now?"
	get_google_rating.short_description="Google Rating"
	get_google_price_level.short_description="Price Level"