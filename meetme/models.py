from django.db import models

class Meetme(models.Model):
	room = models.IntegerField()
	start_time = models.DateTimeField()
	duration = models.IntegerField()
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return str(self.room)
