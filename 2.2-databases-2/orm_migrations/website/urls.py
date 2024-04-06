from django.contrib import admin
from django.urls import include, path
from school.views import students_list
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students_list),
    path('__debug__/', include(debug_toolbar.urls))
]