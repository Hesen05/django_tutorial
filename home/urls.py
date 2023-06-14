from django.urls import path
from home.views import *


urlpatterns = [
    path('', index, name ='index'),
    path('about/', about, name = 'about'),
    path('subscribe/', subscribe, name = 'subscribe'),
    path('contact/', contact, name = 'contact'),
    path('strories/', strories, name = 'strories'),
    path('strories/<slug:slug>/', strories, name = 'strories'),
    path('create_story', create_story),
    path('email-subscirbers/', emailsubscribers),
    path('recipes/', recipes, name = 'recipes'),
    path('single/', single, name = 'single'),

    path('single/<slug:slug>/', single, name = 'single'),
   
]