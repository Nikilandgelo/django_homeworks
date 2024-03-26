from django.urls import path
from calculator.views import show_buter, show_default, show_omlet, show_pasta

urlpatterns = [
    path('', show_default),
    path('omlet/', show_omlet, name="omlet"),
    path('pasta/', show_pasta, name="pasta"),
    path('buter/', show_buter, name="buter")
]