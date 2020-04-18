from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Boletim

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'dashboard/index.html'

class BoletimListView(ListView):
    template_name = 'dashboard/lista.html'
    model = Boletim
    context_object_name = 'boletins'