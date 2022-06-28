
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('', include('user_api.urls')),
    path('admin/', admin.site.urls),
]