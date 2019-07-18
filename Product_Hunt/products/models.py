from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	title = models.CharField(max_length = 255)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to = 'images/')
	icon = models.ImageField(upload_to = 'images/')
	total_votes = models.IntegerField(default = 0)
	body = models.TextField()
	url = models.TextField()
	is_set = models.IntegerField(default = 0)
	likes = models.TextField(default = "")
	hunter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='products')


	def summary(self):
		return self.body[:100]


	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e, %Y')


	def __str__(self):
		return self.title