from django.shortcuts import render
from django.views import generic
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

class EateryListView(generic.ListView):
	model = Eatery

class EateryDetailView(generic.DetailView):
	model = Eatery
