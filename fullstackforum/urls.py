import imp
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import settings

from rest_framework import routers
from thread.urls import router as thread_router
from board.urls import router as board_router


router = routers.DefaultRouter()
router.registry.extend(thread_router.registry)
router.registry.extend(board_router.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="Forum Django",
        default_version="v1",
        description="Example of endpoints with Django",
        contact=openapi.Contact(
            email="germanzittermann@gmail.com"
        )
    ),
    public=True
)

static_urlpatterns = [
    re_path(r"^static/(?P<path>.*", serve, {"document_root": settings.STATIC_ROOT})
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/", include(router.urls)),

    path(
        "doc/",
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
