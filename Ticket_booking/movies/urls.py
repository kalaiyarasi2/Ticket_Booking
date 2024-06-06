from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import Movies_detailsviewsset ,MovieIDChoiceviewsset
router = routers.DefaultRouter()
router.register(r'books', Movies_detailsviewsset())
router.register(r'books', MovieIDChoiceviewsset())


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

