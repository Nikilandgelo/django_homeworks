from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from advertisements.views import AdvertisementViewSet

router = SimpleRouter()
router.register("advertisements", AdvertisementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]