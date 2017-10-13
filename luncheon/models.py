from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

import urllib
import googlemaps
from .apikeys import get_gmaps_api_key

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

	website_link = models.URLField(
		blank=True,
		null=True
	)

	menu_link = models.URLField(
		blank=True,
		null=True
	)

	favorited_by = models.ManyToManyField(User, blank=True)

	# Metadata
	class Meta:
		ordering = ['name']
		verbose_name_plural = 'eateries'

	# Methods
	def get_absolute_url(self):
	    """
	    Returns the url to access a particular instance of the model.
	    """
	    return reverse('eatery-detail', args=[str(self.id)])

	def __str__(self):
		return self.name

	def total_favorites(self):
		return self.favorited_by.count()

	def getGoogleData(self):
		gmapsAPIkey = get_gmaps_api_key()
		gmaps = googlemaps.Client(key=gmapsAPIkey)

		fueledAddress="568 Broadway, New York, NY"
		safeFueledAddress = urllib.parse.quote(fueledAddress, safe='')

		walking_distance = ''
		maps_link = ''
		directions_link = ''
		open_now = 'Unsure!'
		google_rating = ''
		price_level = ''
		
		# calculate walking distance with Distance Matrix API
		if (self.address):
			distance_matrix = gmaps.distance_matrix(fueledAddress, self.address, mode="walking")
			try:
				walking_distance = distance_matrix['rows'][0]['elements'][0]['duration']['text']
			except KeyError:
				pass

		safeAddress = urllib.parse.quote(self.address, safe='')

		# get link to map with location pinned and link to map with directions loaded up
		if safeAddress:
			maps_link = 'https://www.google.com/maps/search/?api=1&query=' + safeAddress
			directions_link = 'https://www.google.com/maps/dir/?api=1&origin=' + safeFueledAddress + '&destination=' + safeAddress

		# get more detailed info from the Google Places API
		geocodedAddress = gmaps.geocode(self.address)
		latLong = geocodedAddress[0]['geometry']['location']

		place_details = gmaps.places(self.name, latLong, 100)

		if (place_details is not None):
			# try to see if restaurant is open now
			try:
				if place_details['results'][0]['opening_hours']['open_now']:
					open_now = 'Yes!'
				else:
					open_now = 'Nope!'
			except KeyError:
				pass

			# try to see if Google has a rating out of 5 for the restaurant
			try:
				if place_details['results'][0]['rating']:
					google_rating = place_details['results'][0]['rating']
			except KeyError:
				pass

			# try to see if Google has a price rating
			try:
				if place_details['results'][0]['price_level']:
					for i in range(place_details['results'][0]['price_level']):
						price_level += '$'
			except KeyError:
				pass

		googleApiDict = {'walking_distance' : walking_distance, 'maps_link' : maps_link, 'directions_link' : directions_link, 'open_now' : open_now, 'google_rating' : google_rating, 'price_level' : price_level}
		
		return googleApiDict
