from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer

from advertisements.filters import AdvertisementFilter

from rest_framework.permissions import IsAuthenticated
from advertisements.permissions import IsOwner

from rest_framework.decorators import action
from advertisements.models import UserFavouriteAdverts
from rest_framework.response import Response

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filterset_class = AdvertisementFilter
    
    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        elif self.action in ["create", "add_to_favourite"]:
            return [IsAuthenticated()]
        else:
            return []
        
    @action(detail=True, methods=['post'])
    def add_to_favourite(self, request, pk) -> Response:
        if request.user == Advertisement.objects.filter(id=pk)[0].creator:
            return Response('Свои обьявления к сожалению нельзя добавлять')
        UserFavouriteAdverts.objects.create(user=request.user, advertisements=Advertisement.objects.filter(id=pk)[0])
        return Response('Обьявление успешно добавлено в избранное')