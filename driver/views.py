from rest_framework import generics
from .models import Driver
from rest_framework.response import Response
from .serializers import DriverSerializer, DriverCreateSerializer

# Create your views here.



class DriverList(generics.ListAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.filter(assigned_truck__isnull=False)

        email = self.request.query_params.get('email', None)
        mobile_number = self.request.query_params.get('mobile_number', None)
        language = self.request.query_params.get('language', None)
        number_plate = self.request.query_params.get('number_plate', None)

        if email:
            queryset = queryset.filter(email=email)
        if mobile_number:
            queryset = queryset.filter(mobile_number=mobile_number)
        if language:
            queryset = queryset.filter(language=language)
        if number_plate:
            queryset = queryset.filter(assigned_truck__number_plate=number_plate)

        return queryset
    

class DriverDetail(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'driver_id'


class DriverCreate(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverCreateSerializer


