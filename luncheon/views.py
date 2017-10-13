from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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
    paginate_by = 10

class EateryDetailView(generic.DetailView):
    model = Eatery

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EateryDetailView, self).get_context_data(**kwargs)
        context['googleData'] = self.get_object().getGoogleData()
        return context

class FavoritedEateriesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Eatery
    template_name = 'luncheon/favorites.html'
    paginate_by = 10

    def get_queryset(self):
        return Eatery.objects.filter(favorited_by=self.request.user)
