from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)
router.register(r'collections', views.CollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
