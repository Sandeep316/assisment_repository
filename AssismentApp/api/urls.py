
from django.conf.urls import url , include
from AssismentApp.api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp',views.ReviewDataView)

urlpatterns = [
    url('',include(router.urls)),
]