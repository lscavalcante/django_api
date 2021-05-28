from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register("v1", ExampleModelViewSet)
router.register("v2", ExampleGenericApi)
# se for cadastrado o parametro basename nāo sera solicitado queryset na classe
router.register("v3", ExampleViewSet, basename='v3')

urlpatterns = [
    path("", include(router.urls)),
    #esse é basseado em funçāo entāo é necessario passar desse modo
    path('only-list', ExampleModelListApi.as_view(), name="only-list"),
    path('example-api-view', ExampleApiView.as_view(), name="example-api-view"),
    # path('only-generic', ExampleGenericApi.as_view(), name="only-generic"),
]