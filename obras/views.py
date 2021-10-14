from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework_csv.renderers import CSVRenderer
from rest_framework_csv.parsers import CSVParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

import pandas as pd

from obras.models import Obras
from obras.serializers import ObrasSerializer, AutorSerializer


class CadastrarListarObraAPIView(ListCreateAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['editora']


class CadastrarObrasCSVAPIView(CreateAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
    parser_classes = [CSVParser, MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        data = request.data['arquivo']
        df = pd.read_csv(data)
        for i in range(len(df)):
            autores_df = df['autores'][i]
            autores_tuple = autores_df.split(",")
            autores = [x.strip(",") for x in autores_tuple if x != ","]
            data = {'titulo': df['titulo'][i],
                    'editora': df['editora'][i],
                    'foto': df['foto'][i],
                    'autores': [AutorSerializer(data=autor).save() for autor in autores if AutorSerializer(data=autor).is_valid()]}
            serializer = self.get_serializer(data=data)
            serializer.is_valid()
            serializer.save()
        return Response()


class GerarArquivoObrasCSVAPIView(ListAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_criacao']
    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [CSVRenderer]


class VisualizarDeletarObraAPIView(RetrieveDestroyAPIView):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer

