from django.conf import settings
from django.db import models

# Create your models here.
class Neighbour(models.Model):
	title = models.CharField(max_length = 20, blank = False)
	description = models.TextField()

	def __unicode__(self):
		return self.title

class Feedback(models.Model):
	RATINGS = (('one','1'),
		   ('two','2'),
		   ('three','3'),
		   ('four','4'),
		('five','5'),)

	user_name = models.OneToOneField(settings.AUTH_USER_MODEL)
	neighbourhoods = models.ForeignKey(Neighbour, related_name ='neighbours')
	phone_number = models.CharField(max_length = 20,blank = False)
	rating = models.CharField(max_length = 5, blank = False, choices = RATINGS)
	comment = models.TextField()

	def __unicode__(self):
		return user_name.username
	
