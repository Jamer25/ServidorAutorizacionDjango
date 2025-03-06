from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # URLs de OAuth2
    path('api/', include('api.urls')),  # Tu API protegida
]


