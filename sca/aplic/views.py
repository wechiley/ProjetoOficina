from django.views.generic import ListView
from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import FuncionarioForm
from aplic.models import Peca
from .models import Peca




def index(request):
    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'   

class PecaView(TemplateView):
    template_name = 'pecas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pecas'] = Peca.objects.all()
        return context
    
    
class SearchPecaView(TemplateView):
    template_name = 'pecas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        print("Query:", query)
        context['pecas'] = Peca.objects.filter(TipoPeca__icontains=query)
        return context
    
class CadastrarFuncionarioView(View):
    template_name = 'cadastrar_funcionario.html'

    def get(self, request, *args, **kwargs):
        form = FuncionarioForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # ou redirecione para a página desejada após o cadastro
        return render(request, self.template_name, {'form': form})   
    
class DetalhesView(ListView):
    template_name = 'detalhes.html'
    paginate_by = 5
    ordering = 'TipoPeca'
    model = Peca

    def get_context_data(self, **kwargs: Any):
        context = super(DetalhesView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['peca'] = Peca.objects.filter(id=id).first()
        return context