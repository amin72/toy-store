from django.urls import path
from drone import views


app_name = 'drone'

urlpatterns = [
    path('vehicle-categories/',
        views.DroneCategoryList.as_view(),
        name=views.DroneCategoryList.name
    ),
    
    path('vehicle-categories/<pk>/',
        views.DroneCategoryDetail.as_view(),
        name=views.DroneCategoryDetail.name
    ),
    
    path('vehicles/',
        views.DroneList.as_view(),
        name=views.DroneList.name
    ),

    path('vehicles/<pk>/',
        views.DroneDetail.as_view(),
        name=views.DroneDetail.name
    ),

    path('pilots/',
        views.PilotList.as_view(),
        name=views.PilotList.name
    ),

    path('pilots/<pk>/',
        views.PilotDetail.as_view(),
        name=views.PilotDetail.name
    ),
    
    path('competitions/',
        views.CompetitionList.as_view(),
        name=views.CompetitionList.name
    ),
    
    path('competitions/<pk>/',
        views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name
    ),
    
    path('',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name
    ),
]
