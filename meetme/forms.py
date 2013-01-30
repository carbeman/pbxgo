from django import forms
from models import Meetme
import random
from django.contrib.admin import widgets   

class MeetmeForm(forms.ModelForm):      
    room = forms.IntegerField()
    start_time = forms.DateTimeField()
    duration = forms.IntegerField()
    description = forms.CharField(max_length=200)

    class Meta:
        model = Meetme

    def __init__(self, *args, **kwargs):
        super(MeetmeForm, self).__init__(*args, **kwargs)

        if kwargs.has_key('instance'):
            instance = kwargs['instance']            
            self.initial['room'] = instance.room  
        else:
            self.initial['room'] = random.randint(10000,99999)  

        self.fields['start_time'].widget = widgets.AdminSplitDateTime()
        self.fields['duration'].widget = forms.Select(choices=[(d, d) for d in range (1,11)])
        self.fields['description'].widget = forms.TextInput(attrs={'size':'80'})

        self.fields['room'].help_text = "Il numero di stanza da digitare al telefono quando verra' richiesto. Non va modificato." 
        self.fields['start_time'].help_text = "Data ed ora d'inizio."
        self.fields['duration'].help_text = "Durata della conferenza espressa in ore."
        self.fields['description'].help_text = "Breve descrizione dell'evento."
