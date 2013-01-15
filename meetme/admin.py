from meetme.models import Meetme
from django.contrib import admin
from forms import MeetmeForm

class MeetmeAdmin(admin.ModelAdmin):
#    readonly_fields = ('room',)
    list_display = ('room','start_date','end_date','description')
    list_filter = ('start_date',)
#    list_editable = ('start_date','end_date')

    def get_form(self, request, obj=None, **kwargs):
        return MeetmeForm


admin.site.register(Meetme, MeetmeAdmin)
