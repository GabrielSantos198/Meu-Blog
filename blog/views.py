from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class Noticias(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status='notícias')
	template_name = 'noticias.html'


class PostView(DetailView):
	model = Post
	template_name = 'detalhes.html'


class Tecnologia(ListView):
	queryset = Post.objects.filter(status='tecnológia')
	template_name = 'tecnologia.html'


class Cultura(ListView):
	queryset = Post.objects.filter(status='cultura')
	template_name = 'cultura.html'


class Tirinha(ListView):
	queryset = Post.objects.filter(status='tirinhas')
	template_name = 'tirinhas.html'


class Motivacao(ListView):
	queryset = Post.objects.filter(status='motivação')
	template_name = 'motivação.html'


class Ciencia(ListView):
	queryset = Post.objects.filter(status='ciência')
	template_name = 'ciência.html'


class Saude(ListView):
	queryset = Post.objects.filter(status='saúde')
	template_name = 'saude.html'


class Viajem(ListView):
	queryset = Post.objects.filter(status='viajem')
	template_name = 'viajem.html'