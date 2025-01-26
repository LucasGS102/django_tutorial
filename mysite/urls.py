from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import settings


urlpatterns = [
        path("", include("polls.urls")),
        path("admin/", admin.site.urls),
] 

if not settings.TESTING:
    urlpatterns += debug_toolbar_urls()

