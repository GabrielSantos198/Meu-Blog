from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import Post
import operator
from functools import reduce

# Create your views here.
class Noticias(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='notícias')
	template_name = 'noticias.html'


class Search(ListView):
	queryset = Post.objects.all()
	paginate_by = 10
	def get_queryset(self):
		result = super(Search, self).get_queryset()
		query = self.request.GET.get('q')
		if query:
			query_list = query.split()
			result = result.filter(
				reduce(operator.and_,
				(Post.objects.get(title__icontains=q) for q in query_list)) |
				reduce(operator.and_,
				(Post.objects.get(content__icontains=q) for q in query_list))
				)
			return result

class PostView(DetailView):
	model = Post
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