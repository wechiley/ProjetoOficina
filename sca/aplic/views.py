from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
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
    


        

    
    

    
    


