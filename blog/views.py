from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import Post
import operator
from functools import reduce
from django.db.models import Q
# Create your views here.

class Principal(ListView):
    paginate_by = 5
    queryset = Post.objects.all().exclude(status='tirinhas')
    template_name = 'index.html'



class Noticias(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='notícias')
	template_name = 'noticias.html'


class Search(ListView):
    queryset = Post.objects.all()
    paginate_by = 10
    template_name = "search.html"

    def get_queryset(self):
        result = super(Search, self).get_queryset()
        query = self.request.GET.get("q")
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_, (Q(title__icontains=x) for x in query_list))
            ) | result.filter(
                reduce(operator.and_, (Q(content__icontains=x) for x in query_list))
            )
        return result


class PostView(DetailView):
	queryset = Post.objects.all().exclude(status='tirinhas')
	template_name = 'detalhes.html'


class Tecnologia(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='tecnológia')
	template_name = 'tecnologia.html'


class Cultura(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='cultura')
	template_name = 'cultura.html'


class Tirinha(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='tirinhas')
	template_name = 'tirinhas.html'


class Motivacao(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='motivação')
	template_name = 'motivação.html'


class Ciencia(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='ciência')
	template_name = 'ciência.html'


class Saude(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='saúde')
	template_name = 'saude.html'


class Viajem(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='viajem')
	template_name = 'viajem.html'



