from django.db import models

class Meetme(models.Model):
	room = models.IntegerField(help_text="testo di supporto")
	start_time = models.DateTimeField()
	duration = models.IntegerField()
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return str(self.room)

	class Meta:
		verbose_name_plural = "Meetme"
