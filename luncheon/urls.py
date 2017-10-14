from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eateries/$', views.EateryListView.as_view(), name='eateries'),
    url(r'^eatery/(?P<pk>\d+)$', views.EateryDetailView.as_view(), name='eatery-detail'),
    url(r'^favorites/$', views.FavoritedEateriesByUserListView.as_view(), name='favorited-by'),
    url(r'^eatery/(?P<pk>[-\w]+)/favorite/$', views.add_favorite_eatery, name='add-favorite-eatery'),
]
