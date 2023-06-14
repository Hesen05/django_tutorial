from django.urls import path
from home.api.views import (CategoryView,
                            StroriesView,
                            CategoryViewSlug)
urlpatterns = [
    
    path('categories/',CategoryView.as_view() , name = 'CategoryView'),
     path('categories/<slug:slug>/',CategoryViewSlug.as_view(), name = 'CategoryViewSlug'),
    path('strories/', StroriesView.as_view(), name = 'strories_api' )


] 