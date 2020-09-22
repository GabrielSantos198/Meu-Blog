from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomePageView(ListView):
	model = Post
	template_name = 'index.html'


class Noticias(ListView):
	queryset = Post.objects.filter(status='Notícias')
	template_name = 'noticias.html'



class Post(DetailView):
	model = Post
	template_name = 'detalhes.html'
