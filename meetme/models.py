from django.db import models
import random

class Meetme(models.Model):
	room = models.IntegerField() #default=random.randint(00000,99999))
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return str(self.room)
