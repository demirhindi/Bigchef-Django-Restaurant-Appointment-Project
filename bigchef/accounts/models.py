from django.db import models
from mainapp.models import Blog
from django.contrib.auth.models import User 

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blogs')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	bodytext = models.TextField(max_length=1000000)
	date = models.DateTimeField(auto_now_add=True)