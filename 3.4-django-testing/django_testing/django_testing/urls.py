from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from students.views import CoursesViewSet

router = SimpleRouter()
router.register("courses", CoursesViewSet, basename="courses")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]