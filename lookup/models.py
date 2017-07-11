from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# Maybe kill this, and add the User model from the auth module?
#class User(models.Model):
#	user_name = models.CharField(max_length=100)
#
#	def __str__(self):
#		return self.user_name

class System(models.Model):
	system_name = models.CharField(max_length=150)
	def __str__(self):
		return self.system_name

class Availability(models.Model):
	availability_name = models.CharField(max_length=150)
	def __str__(self):
		return self.availability_name

class Terrain(models.Model):
	terrain_name = models.CharField(max_length=150)
	def __str__(self):
		return self.terrain_name


class Adventure(models.Model):
	pub_date = models.DateTimeField('date published', default=timezone.now)
	adv_title = models.CharField(max_length=200, default='')
	adv_desc = models.CharField(max_length=500, default='')
	submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
	#ratings = models.ForeignKey(Rating, on_delete=models.CASCADE)
	min_party_size = models.IntegerField(default=4)
	max_party_size = models.IntegerField(default=6)
	min_level = models.IntegerField(default=1)
	max_level = models.IntegerField(default=3)
	
	adv_availability = models.ForeignKey(Availability,default=0)

	adv_cost = models.IntegerField(default=0)

	system = models.ForeignKey(System, default=0)

	terrain = models.ForeignKey(Terrain,default=0)

	publication_year = models.IntegerField(default=2017)
	author = models.CharField(max_length=100, default='')
	source = models.CharField(max_length=200, default='')
	source_url = models.URLField(max_length=500,default='')

	page_count = models.IntegerField(default=25)

	def __str__(self):
		return self.adv_title

	def get_absolute_url(self):
		return reverse('adventure-detail', kwargs={'pk': self.pk})

#	def save(self, *args, **kwargs):
#		self.submitted_by = User
#		super(Adventure, self).save(*args, **kwargs)

	class Meta:
		permissions = (("can_add_adventure", "Add adventure"),("can_edit_all_adventures", "Edit all adventures"),("can_edit_own_adventure", "Edit own adventures"))  

class Rating(models.Model):
	rating = models.IntegerField()
	comments = models.CharField(max_length=200)
	#submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
	adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.rating)



