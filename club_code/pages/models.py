from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
	def __str__(self):
		return str('Review ' + str(self.id))

	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.TextField(max_length=200)
	author = models.TextField(max_length=200)
	illustrator = models.TextField(max_length=200)
	funniest = models.TextField(max_length=500)
	exciting = models.TextField(max_length=500)
	happiest = models.TextField(max_length=500)
	saddest = models.TextField(max_length=500)
	comments = models.TextField(max_length=1500)
	created = models.DateTimeField(auto_now_add=True)
	rating = models.TextField(max_length=2)