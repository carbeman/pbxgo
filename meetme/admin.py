from meetme.models import Meetme
from django.contrib import admin
from forms import MeetmeForm

class MeetmeAdmin(admin.ModelAdmin):

    list_display = ('room','start_time','duration','description')
    ordering = ('-start_time',)
    list_filter = ('start_time',)

    def get_form(self, request, obj=None, **kwargs):
        return MeetmeForm   

admin.site.register(Meetme, MeetmeAdmin)
