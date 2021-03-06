"""fueled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

# code referenced: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# code referenced: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^luncheon/', include('luncheon.urls')),
    url(r'^$', RedirectView.as_view(url='/luncheon/', permanent=True)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

# code referenced: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)