from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r

from obras.models import Obras, Autor
from obras.serializers import ObrasSerializer


class CadastrarListarObraAPIView(ListCreateAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['editora']


class CadastrarObrasCSVAPIView(CreateAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
    parser_classes = [MultiPartParser, FormParser]


class GerarArquivoObrasCSVAPIView(ListAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_criacao']
    parser_classes = [MultiPartParser, FormParser]


class VisualizarDeletarObraAPIView(RetrieveDestroyAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer

