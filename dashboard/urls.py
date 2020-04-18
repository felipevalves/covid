from django.urls import path
from .views import IndexTemplateView, BoletimListView
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('codiv/', BoletimListView.as_view(), name='boletim_list'),

    # path('covid/', views.boletim_list, name='boletim_list')
]