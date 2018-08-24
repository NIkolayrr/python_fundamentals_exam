from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('models', views.CarModelView)
router.register('car', views.CarList)

urlpatterns = [
    path('', include(router.urls))
]
