from django.urls import path
from django.views.generic import detail
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.AllListView.as_view(), name='all'),
    path('detail/<pk>', views.PlateDetailView.as_view(), name='detail'),
    path('add', views.PlateCreate.as_view(), name='add-plate'),
    path('edit/<pk>', views.PlateUpdate.as_view(), name='edit-plate'),
    path('delete/<pk>', views.PlateDelete.as_view(), name='delete-plate'),
    path('regions/', views.RegionList.as_view(), name='region-list'),
    path('region/add', views.RegionCreate.as_view(), name='add-region'),
    path('region/edit/<pk>', views.RegionUpdate.as_view(), name='edit-region'),
]
