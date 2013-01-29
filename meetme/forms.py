from django import forms
from models import Meetme
import random
from django.contrib.admin import widgets   

class MeetmeForm(forms.ModelForm):      
    room = forms.IntegerField(min_value=00000,max_value=99999)
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
        self.fields['description'].widget = forms.TextInput(attrs={'size':'60'})

    def save(self, commit=True):
        model = super(MeetmeForm, self).save(commit=False)

        if commit:
            model.save()

        return model


