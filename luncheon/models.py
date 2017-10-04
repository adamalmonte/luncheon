from django.db import models
import uuid # Required for unique book instances
from django.core.validators import MaxValueValidator, MinValueValidator

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
		primary_key=True
	)
	
	address = models.CharField(
		max_length=255,
		blank=True,
		null=True
	)
	
	googleStarRating = models.IntegerField(
		verbose_name="Star Rating (Google)",
		validators = [
			MaxValueValidator(5),
			MinValueValidator(1)
		],
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
	
	priceLevel = models.IntegerField(
		verbose_name="Price Level",
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
	
	id = models.UUIDField(
		default=uuid.uuid4,
		editable=False
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
	    return reverse('model-detail-view', args=[str(self.id)])

	def __str__(self):
		return self.name

	def walking_distance(self):
		return "1 min"

	def open_now(self):
		return "Yes!"

	open_now.short_description="Open Now?"