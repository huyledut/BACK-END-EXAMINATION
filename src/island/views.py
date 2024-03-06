from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .ultils import get_distance
from .models import Island
from .serializers import IslandSerializer
from .repositorys import IslandRepository

island_repository = IslandRepository(Island)

class IslandView(ModelViewSet):
    queryset = island_repository.get_all()
    serializer_class = IslandSerializer

class IslandListView(GenericAPIView):
    queryset = island_repository.get_all()
    serializer_class = IslandSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('longitude', in_=openapi.IN_QUERY, description='Longitude', type=openapi.TYPE_INTEGER),
        openapi.Parameter('latitude', in_=openapi.IN_QUERY, description='Latitude', type=openapi.TYPE_INTEGER)])
    def get(self, request, *args, **kwargs):
        longitude = request.query_params.get('longitude', None)
        latitude = request.query_params.get('latitude', None)
        if longitude is not None and latitude is not None:
            try:
                islands = list(island_repository.get_list_value())
                islands.sort(key = lambda x: get_distance(float(x['latitude']), float(x['longitude']), float(latitude), float(longitude)))
            except:
                islands = None
        return Response(islands, status=status.HTTP_200_OK)
    
    def post(self, reqest):
        
        return Response(reqest, status=status.HTTP_200_OK)



        