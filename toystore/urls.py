from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # version #1
    path(
        'api/v1/drone/',
        include('drone.urls', namespace='v1')
    ),
    
    path(
        'api-auth/v1/',
        include('rest_framework.urls', namespace='rest_framework_v1')
    ),

    # version #2
    path(
        'api/v2/drone/',
        include('drone.v2.urls', namespace='v2')
    ),
    
    path(
        'api-auth/v2/',
        include('rest_framework.urls', namespace='rest_framework_v2')
    ),
]
