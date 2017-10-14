from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Eatery
from .forms import AddFavoriteEateryForm
import datetime

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
    paginate_by = 10

class EateryDetailView(generic.DetailView):
    model = Eatery

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EateryDetailView, self).get_context_data(**kwargs)
        context['googleData'] = self.get_object().getGoogleData()

        if self.request.user in self.get_object().favorited_by.all():
            context['favoritedByCurrentUser'] = True

        return context

class FavoritedEateriesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Eatery
    template_name = 'luncheon/favorites.html'
    paginate_by = 10

    def get_queryset(self):
        return Eatery.objects.filter(favorited_by=self.request.user)

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
def add_favorite_eatery(request, pk):
    """
    View function for favoriting an eatery
    """
    eatery=get_object_or_404(Eatery, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddFavoriteEateryForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.cleaned_data['confirm_favorite'] is True:
                eatery.favorited_by.add(request.user)

                # redirect to a new URL:
                return HttpResponseRedirect(reverse('favorited-by') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = AddFavoriteEateryForm(initial={'confirm_favorite': True,})

    return render(request, 'luncheon/add_favorite_eatery.html', {'form': form, 'eatery':eatery})