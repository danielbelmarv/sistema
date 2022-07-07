from django.urls import path
from . import views






from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.core.serializers import serialize

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos, name='productos'),
    path('productos/crear', views.crear, name='crear'),
    path('productos/editar/<id>/', views.editar, name='editar'),
    path('eliminar/<id>/', views.eliminar, name='eliminar'),
    path('CatalogoCompleto/',views.CatalogoCompleto,name="CatalogoCompleto"),
    path('indexV3', views.indexV3, name='indexV3'),
    path('FormularioV12/', views.FormularioV12, name="FormularioV12"),
    path('compra/', views.compra, name="compra"),
    path('MicuentaV2/',views.MicuentaV2, name="MicuentaV2"),
    path('MiPedidoV2/',views.MiPedidoV2, name="MiPedidoV2"),
    path('SuscFundV2/',views.SuscFundV2, name="SuscFundV2"),
    path('Suscrito1/',views.Suscrito1, name="Suscrito1"),
    path('Suscrito2/',views.Suscrito2, name="Suscrito2"),
    path('Suscrito3/',views.Suscrito3, name="Suscrito3"),
    
] 
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
