from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eateries/$', views.EateryListView.as_view(), name='eateries'),
    url(r'^eatery/(?P<pk>\d+)$', views.EateryDetailView.as_view(), name='eatery-detail'),
]
