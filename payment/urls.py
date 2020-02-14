from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import *




urlpatterns = [
   #  path(
   #      'country-autocomplete/',
   #      CountryAutocomplete.as_view(),
   #      name='country-autocomplete',
   #  ),
    path('search/', search_users, name='search_users'),
    path('debt/', debt, name='debt'),

]
