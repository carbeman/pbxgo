from django import forms
from models import Meetme
import random
from django.contrib.admin import widgets   

class MeetmeForm(forms.ModelForm):      
    room = forms.IntegerField(min_value=00000,max_value=99999)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    description = forms.CharField(max_length=200)

    class Meta:
        model = Meetme

    def __init__(self, *args, **kwargs):
        super(MeetmeForm, self).__init__(*args, **kwargs)
        self.initial['room'] = random.randint(00000,99999)  
        self.fields['start_date'].widget = widgets.AdminSplitDateTime()
        self.fields['end_date'].widget = widgets.AdminSplitDateTime()
        self.fields['description'].widget = forms.TextInput(attrs={'size':'60'})

    def save(self, commit=True):
        model = super(MeetmeForm, self).save(commit=False)

        if commit:
            model.save()

        return model


