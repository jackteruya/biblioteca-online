from django.urls import path


urlpartterns = [
    path('obras/', CadastrarObraView.as_view(), name="cadastrar-obra"),
    path('upload-obras', CadastrarObrasCSVView.as_view(), name='cadastrar-obras-csv'),
    path('obras/', ListarObrasView.as_view(), name='listar-obras'),
    path('file-obras/', GerarArquivoObrasCSVView.as_view(), name='gerar-obras-csv'),
    path('obras/<int: id>/', VisualizarObraView.as_view(), name='visualizar-obra'),
    path('obras/<int:id>', DeletarObraView.as_view(), name='deletar-obra'),
]
