from django.shortcuts import render
from .models import Eatery

# Create your views here.
def index(request):
	# homepage
	numEateries = Eatery.objects.all().count()
	return render(
		request,
		'index.html',
		context={'numEateries':numEateries},
	)