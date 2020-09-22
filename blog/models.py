from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
	STATUS = (
		('notícias','Notícias'),
		('tecnológia','Tecnológia'),
		('cultura','Cultura'),
		('tirinhas','Tirinhas'),
		('motivação','Motivação'),
		('ciência','Ciência'),
		('saúde','Saúde'),
		('estilo','Estilo'),
		('viajem','Viajem'),
	)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	summary = RichTextField()
	content = RichTextUploadingField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=11,
							  choices=STATUS,
							  default='notícias')

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title
