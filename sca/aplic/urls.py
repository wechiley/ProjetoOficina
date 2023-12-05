from django.conf import settings
from django.urls import path
from .views import IndexView, PecaView, SearchPecaView

from django.conf.urls.static import static
 


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('pecas.html', PecaView.as_view(), name ='pecas'),
    path('search_pecas', SearchPecaView.as_view(), name='search_pecas'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
