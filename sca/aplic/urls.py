from django.conf import settings
from django.urls import include, path
from .views import DetalhesView, IndexView, PecaView, SearchPecaView, CadastrarFuncionarioView
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('pecas.html', PecaView.as_view(), name ='pecas'),
    path('search_pecas', SearchPecaView.as_view(), name='search_pecas'),
    path("<int:id>", DetalhesView.as_view(), name="detalhe_produto"),
    path('cadastrar_funcionario/', CadastrarFuncionarioView.as_view(), name='cadastrar_funcionario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
