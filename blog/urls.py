from django.urls import path

from blog import views

urlpatterns = [
    path('', views.Principal.as_view(), name='principal'),
	path('posts/noticias/', views.Noticias.as_view(), name='noticias'),
	path('posts/noticias/posts/<slug:slug>', views.PostView.as_view(), name='noticias'),
	path('posts/<slug:slug>', views.PostView.as_view(), name='noticias'),
	path('posts/tecnologia/', views.Tecnologia.as_view(), name='tecnologia'),
	path('posts/tecnologia/posts/<slug:slug>', views.PostView.as_view(), name='tecnologia'),
	path('posts/cultura/', views.Cultura.as_view(), name='cultura'),
	path('posts/cultura/posts/<slug:slug>', views.PostView.as_view(), name='cultura'),
	path('posts/tirinhas/', views.Tirinha.as_view(), name='tirinhas'),
	path('posts/tirinhas/posts/<slug:slug>', views.PostView.as_view(), name='tirinhas'),
	path('posts/motivacao/', views.Motivacao.as_view(), name='motivacao'),
	path('posts/motivacao/posts/<slug:slug>', views.PostView.as_view(), name='motivacao'),
	path('posts/ciencia/', views.Ciencia.as_view(), name='ciencia'),
	path('posts/ciencia/posts/<slug:slug>', views.PostView.as_view(), name='ciencia'),
	path('posts/saude/', views.Saude.as_view(), name='saude'),
	path('posts/saude/posts/<slug:slug>', views.PostView.as_view(), name='saude'),
	path('posts/viajem/', views.Viajem.as_view(), name='viajem'),
	path('posts/viajem/posts/<slug:slug>', views.PostView.as_view(), name='viajem'),
	path('search/', views.Search.as_view(), name='blog_search_list_view'),
	path('search/posts/<slug:slug>', views.PostView.as_view(), name="blog_search_list_view"),
]