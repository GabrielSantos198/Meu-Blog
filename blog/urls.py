from django.urls import path

from blog import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
	path('posts/<slug:slug>', views.Post.as_view(), name='post'),
	path('posts/noticias/', views.Noticias.as_view(), name='noticias'),
]