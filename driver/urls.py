from django.urls import path
from .views import DriverList, DriverDetail, DriverCreate, DriverBulkCreateView


urlpatterns = [
    path('driver', DriverList.as_view(), name='driver-list'),
    path('driver/<int:driver_id>', DriverDetail.as_view(), name='driver-detail'),
    path('driver/',DriverCreate.as_view(), name='create-driver' ),
    path('drivers',DriverBulkCreateView.as_view(), name='bulk-drivers')



]
