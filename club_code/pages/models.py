from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
	def __str__(self):
		return str('Review ' + str(self.id))

	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	best = models.TextField(max_length=200)
	worst = models.TextField(max_length=200)
	review = models.TextField(max_length=2000)
	created = models.DateTimeField(auto_now_add=True)
	rating = models.TextField(max_length=2)