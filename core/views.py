from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class MeeiroView(TemplateView):
    template_name = 'meeiro.html'
