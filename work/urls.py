
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    # path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('home.urls')),
    path('api/',include('home.api.urls')),
    path('accounts/', include('accounts.urls'))
)
