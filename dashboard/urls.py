from django.urls import path
from .views import IndexTemplateView, BoletimListView
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('covid/', BoletimListView.as_view(), name='boletim_list'),
    path('dados/', views.importar_dados_covid, name='importar_dados'),

    # path('covid/', views.boletim_list, name='boletim_list')
]