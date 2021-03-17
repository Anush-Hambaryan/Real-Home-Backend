from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django_filters.rest_framework import DjangoFilterBackend

from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]
    filter_backends = [DjangoFilterBackend]

    filter_fields = {
        'owner': ['exact'],

        'transaction': ['exact'],
        'rent_period': ['exact'],
        'currency': ['exact'],    
        'price': ['gte', 'lte'],
        'home_type': ['exact'],
        'year_built': ['gte', 'lte'],
        'area': ['gte', 'lte'],
        'lot_size': ['gte', 'lte'],
        'number_of_rooms': ['exact'],
        'furnishing': ['exact'],
        'district': ['exact'],

        'air_conditioning': ['exact'],
        'washing_machine': ['exact'],
        'central_heating': ['exact'],
        'gas': ['exact'],
        'free_wifi': ['exact'],
        'pwd_accessable': ['exact'],
        'elevator': ['exact'],
        'garage': ['exact'],
        'pool': ['exact'],
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    
        