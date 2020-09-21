from django.urls import path

from blog import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
	path('posts/<int:pk>', views.Post.as_view(), name='post'),
]