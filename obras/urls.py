from django.urls import path

from obras.views import (CadastrarListarObraAPIView, CadastrarObrasCSVAPIView,
                         GerarArquivoObrasCSVAPIView, VisualizarDeletarObraAPIView)


urlpatterns = [
    path('obras/', CadastrarListarObraAPIView.as_view(), name="cadastrar-obra"),
    path('upload-obras', CadastrarObrasCSVAPIView.as_view(), name='cadastrar-obras-csv'),
    path('obras/', CadastrarListarObraAPIView.as_view(), name='listar-obras'),
    path('file-obras/', GerarArquivoObrasCSVAPIView.as_view(), name='gerar-obras-csv'),
    path('obras/<int:pk>/', VisualizarDeletarObraAPIView.as_view(), name='visualizar-obra'),
    path('obras/<int:pk>', VisualizarDeletarObraAPIView.as_view(), name='deletar-obra'),
]
