from django.conf import settings
from django.urls import path
from .views import IndexView, PecaView
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('pecas.html', PecaView.as_view(), name ='pecas')
       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
