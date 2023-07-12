from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='SIBDEV_DEALS',
        default_version='v1',
    ),
    permission_classes=[permissions.AllowAny])

urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('core/', include('core.urls', namespace='core')),
    path('silk/', include('silk.urls', namespace='silk')),
]
