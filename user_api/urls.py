from django.urls import path
from . import views
from django.urls import include

from rest_framework import routers

router = routers.DefaultRouter()
 
router.register(r'user-table', views.UserTableClassView, 'user-table')
router.register(r'user-details', views.UserDetailsTableClassView, 'user-details')
 
urlpatterns = [
    path('api-', include(router.urls)),
]